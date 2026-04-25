
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the superclass
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to the queue
        self.producer_queue.put(payload.decode('utf-8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed:", reason)

# Set up the WebSocket client factory
job_queue = queue.Queue()
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a callable to instantiate

reactor.connectTCP("localhost", 7096, factory)
reactor.run()
