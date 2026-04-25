
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue  # Use 'queue' in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the base class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure bytes are used

    def onOpen(self):
        self.sendHello()
        # Add more logic here to handle incoming messages

    def onMessage(self, payload, isBinary):
        # Decode payload and add to the queue
        message = payload.decode('utf8')
        self.producer_queue.put(message)
        print(f"Added to queue: {message}")

# Creating the factory and setting the protocol
job_queue = queue.Queue()  # Thread-safe queue
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function instead

# Connect the WebSocket client
from autobahn.twisted.websocket import connectWS
connectWS(factory)

# Start the Twisted reactor
reactor.run()
