
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import queue

# Define the WebSocket client protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent class's init
        self.producer_queue = producer_queue

    def onOpen(self):
        self.sendHello()

    def sendHello(self):
        # Send a message indicating the connection is open
        self.sendMessage(b"hello")

    def onMessage(self, payload, isBinary):
        # This is where you handle incoming messages
        # Simulating job processing
        self.producer_queue.put(payload)  # Add the message to the queue
        print(f"Message received and added to queue: {payload}")

# Create a factory for the WebSocket
class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket

# Example usage of the WebSocket client
def start_websocket_client():
    job_queue = queue.Queue()  # Create a thread-safe queue
    factory = MyWebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create a new instance
    connectWS(factory)  # Connect to the WebSocket server

def main():
    start_websocket_client()
    reactor.run()  # Start the Twisted event loop

if __name__ == "__main__":
    main()
