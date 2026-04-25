
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Message must be bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Assuming you're processing incoming messages
        self.producer_queue.put(payload)  # Queue the incoming message

# Setup WebSocket connection
if __name__ == '__main__':
    # Initialize the job queue (Python 3 version)
    job_queue = queue.Queue()

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method

    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()
