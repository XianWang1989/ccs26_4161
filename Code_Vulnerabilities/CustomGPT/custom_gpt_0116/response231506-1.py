
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure the message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message
        self.producer_queue.put(payload.decode('utf8'))  # Add the message to the queue

class MyClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket

def main():
    job_queue = queue.Queue()  # Use queue from the standard library
    factory = MyClientFactory("ws://localhost:7096")

    # Pass the queue to the protocol
    factory.protocol = lambda: BridgeSocket(job_queue)

    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == "__main__":
    main()
