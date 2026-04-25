
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
import queue  # Use the standard library queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure the message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example of pushing incoming messages to the queue
        self.producer_queue.put(payload)

# Setup the factory and connect
def main():
    job_queue = queue.Queue()  # Create a FIFO queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to instantiate the protocol
    connectWS(factory)

    reactor.run()

if __name__ == '__main__':
    main()
