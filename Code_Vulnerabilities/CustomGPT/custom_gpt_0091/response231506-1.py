
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example: add received message to the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed:", reason)

# Create a queue to share between threads
job_queue = Queue()

# Create the factory and assign the custom protocol
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Instantiate here

# Connect the WebSocket
from autobahn.twisted.websocket import connectWS
connectWS(factory)

# Start the Twisted reactor
reactor.run()
