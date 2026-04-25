
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and place them in the queue
        if not isBinary:
            message = payload.decode('utf8')
            self.producer_queue.put(message)
            print(f"Message received and added to queue: {message}")

# Usage example
if __name__ == "__main__":
    job_queue = Queue()

    # Create the factory and specify the WebSocket protocol
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to the WebSocket server
    from twisted.internet import reactor
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()
