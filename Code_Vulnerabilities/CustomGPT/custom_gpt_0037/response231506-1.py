
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted import connectWS
import Queue  # Replace with `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode message to bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example of processing incoming messages
        # Add the received message to the queue
        self.producer_queue.put(payload.decode('utf8'))

# Connection code
factory = WebSocketClientFactory("ws://localhost:7096")
job_queue = Queue.Queue()  # Use 'queue' in Python 3
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function for correct instantiation
connectWS(factory)
