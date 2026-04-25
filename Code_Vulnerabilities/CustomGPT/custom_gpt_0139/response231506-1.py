
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = None  # Initialize the producer queue

    def onOpen(self):
        self.sendHello()

    def sendHello(self):
        self.sendMessage(b"hello")

    def onMessage(self, payload, isBinary):
        # Example of adding received messages to the job queue
        if self.producer_queue:
            self.producer_queue.put(payload)

    def setQueue(self, producer_queue):
        self.producer_queue = producer_queue  # Set the producer queue


class BridgeFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Define the protocol to use

    def __init__(self, url, job_queue):
        super(BridgeFactory, self).__init__(url)
        self.job_queue = job_queue

    def buildProtocol(self, addr):
        protocol = super(BridgeFactory, self).buildProtocol(addr)
        protocol.setQueue(self.job_queue)  # Pass the queue to the protocol
        return protocol


# Usage
job_queue = Queue.Queue()  # Create a queue
factory = BridgeFactory("ws://localhost:7096", job_queue)  # Create the factory
reactor.connectTCP("localhost", 7096, factory)  # Connect to the WebSocket server
reactor.run()
