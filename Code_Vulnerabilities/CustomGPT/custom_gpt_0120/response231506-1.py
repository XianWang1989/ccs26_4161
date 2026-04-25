
from autobahn.twisted.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.defer import Deferred
import queue  # Use 'queue' in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and put them in the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket connection closed: {reason}")

# Factory to create the WebSocket client
class BridgeClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Set the protocol class here

if __name__ == "__main__":
    job_queue = queue.Queue()  # Create the job queue

    factory = BridgeClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method for the protocol

    # Connect WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()
