
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

# Create your job queue
job_queue = queue.Queue()

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = None  # Will be set later

    def set_queue(self, producer_queue):
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you send bytes

    def onOpen(self):
        self.sendHello()
        # More functionality can be added here

    def onMessage(self, payload, isBinary):
        # When you receive a message, add it to the queue
        self.producer_queue.put(payload)

# Custom factory to set the queue
class BridgeSocketFactory(WebSocketClientFactory):
    protocol = BridgeSocket

    def __init__(self, url, queue):
        super().__init__(url)
        self.queue = queue

    def buildProtocol(self, addr):
        proto = self.protocol()
        proto.set_queue(self.queue)  # Set the queue in protocol instance
        return proto

# Setup the WebSocket connection
factory = BridgeSocketFactory("ws://localhost:7096", job_queue)
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
