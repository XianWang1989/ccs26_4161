
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode the message to bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example of putting incoming messages into the queue
        message = payload.decode('utf8')  # Decode the message
        self.producer_queue.put(message)

# Usage example
if __name__ == "__main__":
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Pass the job_queue via a factory method
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to the WebSocket server
    connectWS(factory)

    reactor.run()
