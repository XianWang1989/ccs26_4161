
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send message as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add it to the queue
        self.producer_queue.put(payload.decode('utf8'))

# Example usage
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()  # Use `queue.Queue()` in Python 3
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method to create protocol instances
    connectWS(factory)
