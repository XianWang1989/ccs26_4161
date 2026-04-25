
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet.task import deferLater
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Put the incoming message to the producer_queue
        self.producer_queue.put(payload.decode('utf8'))

# Setup the WebSocket client factory
producer_queue = queue.Queue()
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(producer_queue)  # Create instances via a callable

# Connect the WebSocket
from autobahn.twisted.websocket import connectWS
connectWS(factory)

# Run the reactor
reactor.run()
