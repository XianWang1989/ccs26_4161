
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to the queue
        self.producer_queue.put(payload)

# Factory to create protocol instances
class BridgeSocketFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, address):
        return BridgeSocket(self.producer_queue)

# Set up the queue and factory
job_queue = Queue()
factory = BridgeSocketFactory("ws://localhost:7096", job_queue)

# Connect to the WebSocket server
from twisted.internet import reactor
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
