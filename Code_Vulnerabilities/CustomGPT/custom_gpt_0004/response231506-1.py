
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add it to the queue
        self.producer_queue.put(payload.decode('utf8'))

# Set up the job queue
job_queue = Queue()

# Create a factory
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to call the class correctly

# Connect to the server
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
