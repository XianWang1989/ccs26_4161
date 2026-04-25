
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue  # Use `queue` for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Properly call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here you can add incoming data to the job queue
        self.producer_queue.put(payload)
        # Process the incoming message as needed

# Setting up the WebSocket connection
if __name__ == "__main__":
    job_queue = queue.Queue()  # Create a job queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function for protocol

    # Connecting the WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()
