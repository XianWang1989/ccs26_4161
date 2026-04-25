
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
import Queue  # Or use `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Properly initialize the base class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure to send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here you can handle incoming messages and add them to the queue
        self.producer_queue.put(payload)

# Factory class to connect WebSocket
class JobWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, job_queue):
        super().__init__(url)
        self.protocol = BridgeSocket(job_queue)

if __name__ == "__main__":
    job_queue = Queue.Queue()  # Use queue.Queue() for Python 3
    factory = JobWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)  # connectWS function should be defined/imported
    reactor.run()
