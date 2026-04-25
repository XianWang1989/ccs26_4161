
from twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import queue  # Use the built-in queue module


class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Note the 'b' for byte string

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and put them on the queue.
        self.producer_queue.put(payload)
        # Handle binary or text message accordingly.
        # Additional processing can go here.


if __name__ == "__main__":
    job_queue = queue.Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Assign the class rather than an instance
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)
    reactor.run()
