
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import Queue  # Use `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Properly initialize the superclass
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()
        # You can put your logic to handle incoming messages here

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and add to queue
        self.producer_queue.put(payload)

# Setup and connect the WebSocket
factory = WebSocketClientFactory("ws://localhost:7096")
job_queue = Queue.Queue()  # Use queue.Queue() in Python 3
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a callable for factory.protocol
connectWS(factory)

reactor.run()
