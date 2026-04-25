
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import Queue  # or `from queue import Queue` for Python 3.x
import threading

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes

    def onOpen(self):
        self.sendHello()
        print("Connection opened.")

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to queue
        if not isBinary:
            message = payload.decode('utf8')  # Decode the message
            self.producer_queue.put(message)   # Put message in the queue
            print("Message received and added to queue:", message)

    def onClose(self, wasClean, code, reason):
        print("Connection closed:", reason)

# Main function to set up the client
def main():
    job_queue = Queue.Queue()  # Create a queue for passing messages
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Override the protocol in the factory dynamically
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)  # Connect using the custom factory
    reactor.run()  # Start the reactor loop

if __name__ == "__main__":
    main()
