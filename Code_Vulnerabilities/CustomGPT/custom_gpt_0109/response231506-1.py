
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue  # Use the built-in queue module

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure the message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages
        self.producer_queue.put(payload)  # Add incoming message to the queue

def main():
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()  # Use queue.Queue for thread-safe queue
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)
    reactor.run()

if __name__ == '__main__':
    main()
