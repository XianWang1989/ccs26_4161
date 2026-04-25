
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.util import connectWS
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass's __init__
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to the job queue
        self.producer_queue.put(payload.decode('utf8'))

# Create a job queue
job_queue = Queue()

# Define the factory
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to instantiate the protocol

# Connect to the WebSocket server
connectWS(factory)

# Start the reactor
reactor.run()
