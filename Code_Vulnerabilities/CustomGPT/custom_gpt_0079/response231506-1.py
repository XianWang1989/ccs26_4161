
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue  # Use the standard library Queue
from autobahn.twisted.util import sleep  # For asyncio compatibility

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call to the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure to send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming data to the queue
        self.producer_queue.put(payload.decode('utf8'))
        print(f'Received message: {payload.decode("utf8")}')

# Function to connect using the provided factory
def connect():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method for instantiation
    reactor.connectTCP("localhost", 7096, factory)

# Start the Twisted reactor
connect()
reactor.run()
