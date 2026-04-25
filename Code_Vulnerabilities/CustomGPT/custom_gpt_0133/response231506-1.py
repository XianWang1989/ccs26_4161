
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self):
        super().__init__()  # Ensure the base class is initialized
        self.producer_queue = None  # Will be set later

    def onOpen(self):
        self.sendHello()

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encoding the message

    def setQueue(self, producer_queue):
        self.producer_queue = producer_queue

    def onMessage(self, payload, isBinary):
        if self.producer_queue is not None:
            # Example: put incoming messages into the queue
            self.producer_queue.put(payload.decode('utf8'))

class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Use the class, not an instance

    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        protocol = super().buildProtocol(addr)
        protocol.setQueue(self.producer_queue)
        return protocol

if __name__ == "__main__":
    job_queue = queue.Queue()  # Use Python's built-in queue
    factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)
    reactor.run()
