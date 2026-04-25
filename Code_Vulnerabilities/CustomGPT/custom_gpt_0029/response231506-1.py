
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import Queue  # Use `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()
        # Further logic to handle incoming messages
        self.factory.register(self)  # Register this socket instance

    def onMessage(self, payload, isBinary):
        # Handle the incoming message and add to the queue
        self.producer_queue.put(payload.decode('utf-8'))  # Add message to queue

# Set up the WebSocket client
job_queue = Queue.Queue()  # Use queue.Queue() in Python 3
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function for instance creation

# Connect the WebSocket
from twisted.internet import reactor
from autobahn.twisted.websocket import connectWS

connectWS(factory)
reactor.run()
