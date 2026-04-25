
from twisted.web.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from autobahn.twisted.websocket import connectWS
import queue  # Use `queue` module for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure the base class is initialized
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode to bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        message = payload.decode('utf8')  # Decode received message
        self.producer_queue.put(message)  # Add message to the queue

# Main setup
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)

    reactor.run()
