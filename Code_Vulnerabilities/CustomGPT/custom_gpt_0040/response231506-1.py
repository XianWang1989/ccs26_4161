
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Put incoming message into the queue
        self.producer_queue.put(payload.decode('utf-8'))

# Instantiate your job queue
job_queue = Queue()

# Define a factory, passing the queue to the protocol's constructor
class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Set the protocol class

# Create a factory instance
factory = MyWebSocketClientFactory("ws://localhost:7096")

# Override the factory's protocol instance creation
def buildProtocol(factory):
    return factory.protocol(job_queue)

factory.buildProtocol = buildProtocol

# Connect to the WebSocket server
from twisted.internet import reactor

reactor.connectTCP("localhost", 7096, factory)
reactor.run()
