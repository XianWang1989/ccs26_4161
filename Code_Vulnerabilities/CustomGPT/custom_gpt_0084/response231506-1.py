
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure proper initialization
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the queue
        self.producer_queue.put(payload.decode('utf8'))

if __name__ == "__main__":
    job_queue = queue.Queue()  # Use `queue.Queue` for Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to the WebSocket server
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()
