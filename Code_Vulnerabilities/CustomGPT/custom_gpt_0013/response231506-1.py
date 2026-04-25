
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from queue import Queue
from twisted.internet import reactor

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        # Initialize parent class
        super().__init__()  
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is byte-encoded

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming message to the queue
        self.producer_queue.put(payload)

def main():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method to create instances
    connectWS(factory)

    reactor.run()

if __name__ == "__main__":
    main()
