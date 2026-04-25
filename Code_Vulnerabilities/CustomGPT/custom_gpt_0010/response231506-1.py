
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
import queue as Queue  # Use 'queue' in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure the base class is initialized
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure the message is encoded

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example of pushing received messages to the queue
        self.producer_queue.put(payload.decode('utf8'))  # Decode and store message

def main():
    job_queue = Queue.Queue()  # Create a job queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function

    # Connect the websocket
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == "__main__":
    main()
