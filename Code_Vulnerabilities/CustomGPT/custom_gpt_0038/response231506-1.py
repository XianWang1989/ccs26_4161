
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        # Call the superclass constructor
        super().__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages
        if not isBinary:
            message = payload.decode('utf8')
            self.producer_queue.put(message)  # Add message to the queue

def start_client(job_queue):
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to instantiate the protocol
    connectWS(factory)

# Usage
if __name__ == "__main__":
    job_queue = Queue()
    start_client(job_queue)
    reactor.run()
