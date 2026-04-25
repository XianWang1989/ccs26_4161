
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example of how to process incoming messages
        self.producer_queue.put(payload.decode('utf-8'))  # Add message to the queue

class CustomWebSocketFactory(WebSocketClientFactory):
    def __init__(self, url, job_queue):
        super().__init__(url)
        self.protocol = BridgeSocket(job_queue)

if __name__ == '__main__':
    job_queue = queue.Queue()
    factory = CustomWebSocketFactory("ws://localhost:7096", job_queue)

    # Connect to the WebSocket server
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()
