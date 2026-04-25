
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import Queue  # Use `queue` for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the super class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send bytes for WebSocket

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming message to the job queue
        self.producer_queue.put(payload)

class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Specify the protocol class here

    def __init__(self, url, producer_queue):
        super(MyWebSocketClientFactory, self).__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        # Override to instantiate BridgeSocket with the queue
        return self.protocol(self.producer_queue)

# Usage
if __name__ == '__main__':
    job_queue = Queue.Queue()  # Use `queue.Queue()` for Python 3
    factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)  # You need to import the function

    reactor.run()
