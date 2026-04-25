
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
from twisted.internet import reactor
import queue  # Use 'queue' for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for messages

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload.decode("utf-8"))  # Assuming payload is UTF-8 encoded text

# Factory for the WebSocket connection
class BridgeSocketFactory(WebSocketClientFactory):
    protocol = BridgeSocket

def main():
    job_queue = queue.Queue()
    factory = BridgeSocketFactory("ws://localhost:7096")
    factory.producer_queue = job_queue  # Pass the queue to the factory

    # Connect to the WebSocket server
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    main()
