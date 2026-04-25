
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for message

    def onOpen(self):
        self.sendHello()
        # Implement receiving and processing messages here
        # Example: self.producer_queue.put(message)

# Create a WebSocket client factory
def main():
    job_queue = queue.Queue()  # Use queue.Queue() for Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Override the buildProtocol method to provide your BridgeSocket
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    main()
