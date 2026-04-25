
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class constructor
        self.producer_queue = producer_queue

    def onOpen(self):
        self.sendHello()

    def sendHello(self):
        self.sendMessage(b"hello")  # Send 'hello' message 

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the job queue
        self.producer_queue.put(payload.decode('utf8'))  # Assuming text messages

# Setup the WebSocket client factory
job_queue = queue.Queue()
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function for protocol

connectWS(factory)
reactor.run()
