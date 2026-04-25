
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        # Call the parent class's __init__ method
        super().__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Note: Send message as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload.decode('utf-8'))

# Connection code
if __name__ == "__main__":
    job_queue = queue.Queue()  # Python 3 Queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method
    connectWS(factory)
    reactor.run()
