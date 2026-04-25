
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's __init__ method
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure the message is encoded

    def onOpen(self):
        self.sendHello()
        # Implement any additional logic to handle incoming messages
        self.factory = self.factory  # Reference to the factory to access job_queue

    def onMessage(self, payload, isBinary):
        # Put incoming messages into the queue
        self.producer_queue.put(payload.decode('utf8'))

# Usage
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to instantiate the protocol

    connectWS(factory)
    reactor.run()
