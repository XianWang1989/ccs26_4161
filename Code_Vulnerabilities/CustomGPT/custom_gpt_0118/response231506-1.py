
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted import connectWS
from twisted.internet import reactor
import queue  # Use the queue module for Python 3 compatibility

# Custom WebSocket client protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode to bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf8'))  # Decode from bytes

# Setup WebSocket client factory
def main():
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()  # Create a job queue
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to instantiate the protocol
    connectWS(factory)

    reactor.run()  # Start the Twisted event loop

if __name__ == "__main__":
    main()
