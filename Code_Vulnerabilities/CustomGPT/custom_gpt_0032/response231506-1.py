
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the super constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()
        # You can add more logic to handle incoming messages
        print("WebSocket connection opened.")

    def onMessage(self, payload, isBinary):
        # When a message is received, store it in the queue
        self.producer_queue.put(payload.decode('utf8'))  # Assuming messages are UTF-8 strings
        print("Message received and added to queue.")

# Main function to set up the connection
def main():
    job_queue = queue.Queue()  # Create a thread-safe queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create an instance

    connectWS(factory)  # Establish the WebSocket connection
    reactor.run()  # Start the Twisted event loop

if __name__ == "__main__":
    main()
