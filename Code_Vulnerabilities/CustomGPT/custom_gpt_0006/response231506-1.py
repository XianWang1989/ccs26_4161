
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from autobahn.twisted import connectWS
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is in bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Put incoming messages in the queue
        self.producer_queue.put(payload)

# Create a job queue
job_queue = queue.Queue()

# Create the WebSocket client factory
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to properly instantiate the class

# Connect to the WebSocket
connectWS(factory)

# Start the Twisted reactor
reactor.run()
