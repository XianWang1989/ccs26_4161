
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's __init__ method
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the queue
        self.producer_queue.put(payload)

class MyWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        return BridgeSocket(self.producer_queue)

# Usage
job_queue = Queue()
factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)
connectWS(factory)
reactor.run()
