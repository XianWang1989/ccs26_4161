
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import Queue  # or 'from queue import Queue' for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages
        self.producer_queue.put(payload.decode('utf-8'))

def main():
    job_queue = Queue.Queue()  # Create the job queue
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Set the protocol instance
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to WebSocket
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()

if __name__ == '__main__':
    main()
