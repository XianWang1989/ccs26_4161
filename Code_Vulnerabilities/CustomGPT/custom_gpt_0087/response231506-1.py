
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
import queue  # Use this for Python 3
import threading

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass's initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send bytes, so prefix with b

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload.decode('utf8'))  # Assuming it's a UTF-8 encoded string

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed:", reason)

def main():
    # Create a job queue
    job_queue = queue.Queue()

    # Create the factory and assign the protocol
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect the WebSocket
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()

# Run the main function
if __name__ == "__main__":
    main()
