
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
import Queue  # Use `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the base class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode the message

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add received message to the queue
        self.producer_queue.put(payload.decode('utf8'))

# Main connection code
job_queue = Queue.Queue()  # Use queue.Queue() for Python 3
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method for the protocol

connectWS(factory)
reactor.run()
