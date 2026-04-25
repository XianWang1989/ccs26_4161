
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import sleep
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import Queue  # For Python 2.x, use queue for Python 3.x

# Your WebSocket Protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and enqueue them
        self.producer_queue.put(payload.decode('utf-8'))

# Set up the factory and connection
def run():
    job_queue = Queue.Queue()  # Replace with queue.Queue() if using Python 3.x
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == "__main__":
    run()
