
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()
        # Here you can process incoming messages or manage the queue

    def onMessage(self, payload, isBinary):
        # Example of adding received messages to the queue
        self.producer_queue.put(payload)
        print("Message received and added to queue:", payload)

# Usage
if __name__ == '__main__':
    job_queue = queue.Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory for protocol instantiation

    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()
