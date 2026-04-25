
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.util import reconnect
from twisted.internet import reactor
import Queue  # or `from queue import Queue` for Python 3

# WebSocket Client Protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to queue
        self.producer_queue.put(payload)

# Factory to create the WebSocket client
class BridgeSocketFactory(WebSocketClientFactory):
    protocol = BridgeSocket

def main():
    job_queue = Queue.Queue()  # Create a Queue instance
    factory = BridgeSocketFactory("ws://localhost:7096")  # Use custom factory

    # Set up connection
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == "__main__":
    main()
