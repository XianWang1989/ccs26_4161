
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import Queue  # Use 'queue' for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure byte string

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Enqueue the incoming message
        self.producer_queue.put(payload.decode('utf-8'))

# Create the queue and connect the WebSocket
if __name__ == "__main__":
    job_queue = Queue.Queue()  # Or `queue.Queue()` for Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances

    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()
