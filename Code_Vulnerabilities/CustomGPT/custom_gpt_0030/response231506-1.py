
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.endpoints import clientFromString
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    # Handle incoming messages
    def onMessage(self, payload, isBinary):
        self.producer_queue.put(payload.decode('utf8'))

def main():
    job_queue = queue.Queue()  # Thread-safe queue for jobs
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()

if __name__ == "__main__":
    main()
