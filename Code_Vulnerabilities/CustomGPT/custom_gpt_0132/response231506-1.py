
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure message is byte-encoded

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages; add to the job queue.
        self.producer_queue.put(payload.decode('utf8'))  # Decode if needed
        # Process the data as required.

# Usage example
def start_client():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    start_client()
