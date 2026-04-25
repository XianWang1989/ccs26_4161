
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to queue
        self.producer_queue.put(payload.decode('utf8'))

# Connecting to the WebSocket server
if __name__ == "__main__":
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Set the protocol class rather than an instance
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)
    reactor.run()
