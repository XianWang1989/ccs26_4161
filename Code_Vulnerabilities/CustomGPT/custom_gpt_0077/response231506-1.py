
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the base class correctly
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send a bytes message

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example: Add incoming messages to the queue
        self.producer_queue.put(payload.decode('utf-8'))

# Main code to set up the WebSocket connection
if __name__ == "__main__":
    job_queue = queue.Queue()  # Use queue.Queue() for Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function to instantiate

    connectWS(factory)
    reactor.run()
