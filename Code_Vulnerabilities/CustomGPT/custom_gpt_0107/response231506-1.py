
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and enqueue
        self.producer_queue.put(payload.decode('utf8'))  # Decode bytes to str

# Factory class
class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Specify the protocol class

# Connection code
if __name__ == "__main__":
    job_queue = Queue.Queue()
    factory = MyWebSocketClientFactory("ws://localhost:7096")

    # Pass job_queue via protocol's constructor
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a callable to create protocol instances

    connectWS(factory)  # Use connectWS from Autobahn Twisted
    reactor.run()  # Start the Twisted reactor
