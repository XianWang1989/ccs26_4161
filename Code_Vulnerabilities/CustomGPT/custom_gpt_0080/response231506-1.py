
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from queue import Queue  # For Python 3
from twisted.internet import reactor

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure the parent constructor is called
        self.producer_queue = producer_queue

    def send_hello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.send_hello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the queue
        self.producer_queue.put(payload.decode('utf8'))

def setup_websocket_client():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    setup_websocket_client()
