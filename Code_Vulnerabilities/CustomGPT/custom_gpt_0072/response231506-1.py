
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import Queue  # Use 'import queue' for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        # Call the parent constructor
        super(BridgeSocket, self).__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload.decode('utf8'))

# Initialize the WebSocket factory and job queue
job_queue = Queue.Queue()  # Use 'Queue.Queue()' for Python 2 and 'queue.Queue()' for Python 3
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method

# Connect to the WebSocket
connectWS(factory)

# Start the Twisted reactor
reactor.run()
