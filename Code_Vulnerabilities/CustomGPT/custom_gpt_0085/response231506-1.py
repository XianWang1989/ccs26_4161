
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Enqueue incoming messages into the queue
        self.producer_queue.put(payload.decode('utf8'))

def start_client():
    job_queue = queue.Queue()  # Use the standard library queue

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory to create protocol instances
    connectWS(factory)

    reactor.run()

if __name__ == "__main__":
    start_client()
