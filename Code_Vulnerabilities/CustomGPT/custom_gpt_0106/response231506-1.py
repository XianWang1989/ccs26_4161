
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and put them in the queue
        self.producer_queue.put(payload)

        # Example of how to print the received message
        print(f"Received message: {payload.decode('utf-8')}")

# Application code to set up the WebSocket client
if __name__ == "__main__":
    job_queue = Queue()  # Create a job queue

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda for instantiation

    reactor.connectURL(factory)
    reactor.run()
