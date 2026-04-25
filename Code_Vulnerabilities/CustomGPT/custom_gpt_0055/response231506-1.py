
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()
        # You can now push to the queue with incoming data or whenever necessary

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to the queue
        self.producer_queue.put(payload.decode('utf8'))  # Decode bytes to string

def run_websocket_client():
    job_queue = Queue()

    # Create a factory and assign the protocol
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances

    # Connect to the server
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    run_websocket_client()
