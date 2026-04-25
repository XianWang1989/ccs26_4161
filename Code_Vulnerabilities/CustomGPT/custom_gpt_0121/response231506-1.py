
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from autobahn.twisted.websocket import connectWS
import queue  # Use 'queue' for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Note the 'b' for byte string

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming message to the queue
        self.producer_queue.put(payload.decode('utf-8'))

def main():
    # Create a job queue
    job_queue = queue.Queue()

    # Create the WebSocket client factory
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function

    # Connect to the WebSocket server
    connectWS(factory)

    # Start the reactor
    reactor.run()

if __name__ == "__main__":
    main()
