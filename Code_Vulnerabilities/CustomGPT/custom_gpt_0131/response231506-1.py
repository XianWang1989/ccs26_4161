
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Make sure the message is in bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and queue them
        self.producer_queue.put(payload)

factory = WebSocketClientFactory("ws://localhost:7096")
job_queue = queue.Queue()  # Use `queue.Queue()` for Python 3
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instance

# Connect to WebSocket
from autobahn.twisted.websocket import connectWS
connectWS(factory)

reactor.run()
