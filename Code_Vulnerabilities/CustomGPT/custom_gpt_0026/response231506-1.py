
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
from queue import SimpleQueue  # Use `queue.Queue` for Python 2.x or `queue.SimpleQueue` for Python 3.x

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure that the parent class is initialized
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf-8'))  # Decode the bytes to string

# Main connection code
def main():
    job_queue = SimpleQueue()  # Create a job queue

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function to create the protocol

    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    main()
