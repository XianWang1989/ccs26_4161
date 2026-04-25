
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from autobahn.twisted.websocket import connectWS
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for the message

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here you can handle incoming messages and put them in the queue
        self.producer_queue.put(payload)  # Add incoming data to the queue

# Usage
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()  # Use queue.Queue for Python 3
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)
    reactor.run()
