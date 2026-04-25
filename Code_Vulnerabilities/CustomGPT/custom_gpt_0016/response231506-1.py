
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from queue import Queue
import json

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call to the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure to encode string

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Assuming this is where you want to process incoming messages
        message = payload.decode('utf8')
        self.producer_queue.put(message)  # Put the message in the queue
        print(f'Received and queued: {message}')

    def onClose(self, wasClean, code, reason):
        print(f'WebSocket connection closed: {reason}')

# Setup the factory and connection
job_queue = Queue()

# Define the factory and set the protocol
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)

# Connect to WebSocket
reactor.connectTCP("localhost", 7096, factory)
reactor.run()
