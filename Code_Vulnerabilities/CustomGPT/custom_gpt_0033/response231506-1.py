
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the base class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()
        # You can start processing the job queue or set up listeners here.

    def onMessage(self, payload, isBinary):
        # Process incoming messages and put them into the queue
        self.producer_queue.put(payload.decode('utf-8'))

if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = Queue()
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()
