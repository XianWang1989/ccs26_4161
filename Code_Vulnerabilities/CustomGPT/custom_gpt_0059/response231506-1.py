
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages
        self.producer_queue.put(payload.decode('utf-8'))

# Custom factory class to instantiate the BridgeSocket
class CustomWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Set the protocol class

# Main code to run the WebSocket client
if __name__ == "__main__":
    job_queue = Queue()
    factory = CustomWebSocketClientFactory("ws://localhost:7096")
    factory.protocol = BridgeSocket(job_queue)  # Pass the queue to your protocol

    connectWS(factory)
    reactor.run()
