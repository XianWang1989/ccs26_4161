
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the super class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure to send bytes

    def onOpen(self):
        self.sendHello()
        # Example of receiving a message and putting it in the queue
        self.sendMessage(b"Ready to receive data...")

    def onMessage(self, payload, isBinary):
        # Assuming you want to add the message to the queue
        message = payload.decode('utf8')
        self.producer_queue.put(message)

        # You can handle your incoming messages here
        print("Message received and added to the queue:", message)

def main():
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()  # Use the standard library queue
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances

    # Connect to WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()

if __name__ == "__main__":
    main()
