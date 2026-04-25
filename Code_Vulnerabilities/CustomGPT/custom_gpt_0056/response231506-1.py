
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Properly call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and populate the queue
        self.producer_queue.put(payload)

class BridgeSocketFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Set the protocol to the custom class

    def __init__(self, url, job_queue):
        super(BridgeSocketFactory, self).__init__(url)
        self.job_queue = job_queue

    def buildProtocol(self, addr):
        return self.protocol(self.job_queue)  # Pass the job queue to the protocol

# Usage
job_queue = Queue.Queue()
factory = BridgeSocketFactory("ws://localhost:7096", job_queue)
connectWS(factory)
reactor.run()
