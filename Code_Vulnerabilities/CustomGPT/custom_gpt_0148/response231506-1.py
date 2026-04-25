
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
import queue

# The BridgeSocket class
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the base class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages
        self.producer_queue.put(payload.decode('utf8'))

# The WebSocketClientFactory subclass
class MyWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.protocol = lambda: BridgeSocket(producer_queue)  # Use a callable to instantiate the protocol

# Create a producer queue
producer_queue = queue.Queue()

# Create a factory with the job queue
factory = MyWebSocketClientFactory("ws://localhost:7096", producer_queue)

# Start the connection
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
