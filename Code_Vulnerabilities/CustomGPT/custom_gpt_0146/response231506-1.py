
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()
        # Here you could also start listening for incoming messages,
        # and adding them to the job_queue if necessary.

    def onMessage(self, payload, isBinary):
        # Example of adding incoming messages to the job queue
        self.producer_queue.put(payload.decode('utf8'))

# Set up your job queue
job_queue = Queue()

# Create the WebSocket factory and assign the protocol
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function

# Connect the WebSocket
from autobahn.twisted.websocket import connectWS
connectWS(factory)

# Start the Twisted reactor
reactor.run()
