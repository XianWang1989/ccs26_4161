
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from queue import Queue
import json

# Define your protocol class
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example of processing incoming messages
        data = json.loads(payload)
        self.producer_queue.put(data)  # Add data to the queue
        print("Message received and added to job queue:", data)

# Function to start the WebSocket connection
def start_connection():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function to create protocol instances
    connectWS(factory)

# Run the connection
if __name__ == "__main__":
    start_connection()
    reactor.run()
