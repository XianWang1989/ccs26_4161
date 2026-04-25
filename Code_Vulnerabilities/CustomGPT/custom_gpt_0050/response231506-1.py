
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted import connectWS
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the base class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for message

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and add them to the queue
        message = payload.decode('utf8')  # Decode byte message
        self.producer_queue.put(message)    # Put message in queue
        print(f"Message received: {message}")

# Main application setup
if __name__ == "__main__":
    job_queue = queue.Queue()  # Initialize a thread-safe queue
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Set the protocol to an instance of BridgeSocket
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Start the WebSocket connection
    connectWS(factory)
    reactor.run()
