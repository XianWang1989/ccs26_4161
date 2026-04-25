
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Assuming you want to queue messages received from WebSocket
        self.producer_queue.put(payload.decode('utf8'))

# Usage example
if __name__ == "__main__":
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Set the protocol class
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect
    connectWS(factory)

    reactor.run()
