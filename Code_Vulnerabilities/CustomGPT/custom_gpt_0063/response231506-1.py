
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
import queue
from twisted.internet import reactor

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload)

# Create a factory class to instantiate BridgeSocket
class BridgeSocketFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # This tells the factory what protocol to use

    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        return self.protocol(self.producer_queue)

# Main connection code
def main():
    job_queue = queue.Queue()  # Use standard queue for Python 3
    factory = BridgeSocketFactory("ws://localhost:7096", job_queue)
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    main()
