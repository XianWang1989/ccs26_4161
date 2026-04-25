
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # You can put the incoming message in the job queue
        self.producer_queue.put(payload.decode('utf8'))

def onConnect(factory):
    print("WebSocket connection open")

@inlineCallbacks
def connect():
    job_queue = queue.Queue()  # Initialize the job queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function to instantiate
    connectWS(factory)
    reactor.run()

# Call the connect function to start the process
connect()
