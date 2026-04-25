
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self):
        super().__init__()  # Call the parent class's __init__
        self.producer_queue = None  # Initialize it later

    def setQueue(self, producer_queue):
        """Set the producer queue to share it with the main thread."""
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode message as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here you could put incoming messages into the queue
        if not isBinary:
            message = payload.decode('utf8')
            if self.producer_queue:
                self.producer_queue.put(message)
            print(f"Message received: {message}")

# Usage example
factory = WebSocketClientFactory("ws://localhost:7096")
job_queue = Queue()
bridge_socket = BridgeSocket()
bridge_socket.setQueue(job_queue)  # Set the queue

# This binds your socket class to the factory
factory.protocol = lambda: bridge_socket  # Use a lambda to create instances

# Connect to the WebSocket server
connectWS(factory)

# Start the Twisted reactor
reactor.run()
