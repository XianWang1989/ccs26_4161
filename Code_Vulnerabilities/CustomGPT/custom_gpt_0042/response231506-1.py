
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from queue import Queue
import json

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call to parent class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()
        self.factory = self.factory  # Access factory to send messages

    def onMessage(self, payload, isBinary):
        # Handle incoming messages
        message = payload.decode('utf8')
        self.producer_queue.put(message)  # Put the message into the queue
        # You can also process the message here if needed

def main():
    job_queue = Queue()

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method

    reactor.connectTCP('localhost', 7096, factory)
    reactor.run()

if __name__ == "__main__":
    main()
