
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
import queue

# Define your custom WebSocket client protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for sending messages

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming message to the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed: ", reason)

# Create a factory for your WebSocket connection
class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket

# Set up the job queue
job_queue = queue.Queue()

# Create a factory instance and connect
factory = MyWebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a callable to set the protocol

# Connect the factory
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
