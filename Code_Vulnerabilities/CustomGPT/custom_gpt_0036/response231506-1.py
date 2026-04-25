
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

# Define your WebSocket client protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Correctly call the parent class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Assume the incoming message is a string
        message = payload.decode('utf8')
        self.producer_queue.put(message)  # Put the message in the queue
        print(f"Received and queued message: {message}")

# The factory class for creating socket instances
class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Set the protocol

def main():
    job_queue = Queue()  # Initialize the job queue
    factory = MyWebSocketClientFactory("ws://localhost:7096")  # Create factory instance
    factory.protocol = lambda: BridgeSocket(job_queue)  # Instantiate the protocol with the queue

    # Connect the WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    # Start the reactor
    reactor.run()

if __name__ == "__main__":
    main()
