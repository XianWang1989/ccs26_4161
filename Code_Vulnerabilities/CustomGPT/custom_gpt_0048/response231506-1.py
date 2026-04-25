
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf8'))

def create_protocol(producer_queue):
    class CustomClientFactory(WebSocketClientFactory):
        protocol = BridgeSocket

        def buildProtocol(self, *args, **kwargs):
            return self.protocol(producer_queue)

    return CustomClientFactory

# Setup the queue and factory
job_queue = queue.Queue()
factory = create_protocol(job_queue)("ws://localhost:7096")

# Connect the WebSocket
from autobahn.twisted.websocket import connectWS
connectWS(factory)

# Start the Twisted reactor
reactor.run()
