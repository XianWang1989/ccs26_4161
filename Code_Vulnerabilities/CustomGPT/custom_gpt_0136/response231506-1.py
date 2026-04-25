
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and add them to the job queue
        self.producer_queue.put(payload.decode('utf8'))

# Create a job queue
job_queue = queue.Queue()

# Create the factory and use your custom protocol class
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory for the protocol

# Connect to the WebSocket server
from autobahn.twisted.websocket import connectWS
connectWS(factory)

# Start the Twisted reactor
reactor.run()
