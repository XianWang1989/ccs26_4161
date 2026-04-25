
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure the message is bytes

    def onOpen(self):
        self.sendHello()
        # Add more logic to handle incoming messages and populate the job queue

# Setup WebSocket client factory and connection
factory = WebSocketClientFactory("ws://localhost:7096")
job_queue = Queue()
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function for the protocol
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
