
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming message to job queue
        self.producer_queue.put(payload.decode('utf8'))

# Create the WebSocket client factory
factory = WebSocketClientFactory("ws://localhost:7096")
job_queue = queue.Queue()
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances correctly

# Connect to the WebSocket
from autobahn.twisted.websocket import connectWS
connectWS(factory)
reactor.run()
