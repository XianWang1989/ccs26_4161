
import asyncio
from queue import Queue
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure the base class is initialized
        self.producer_queue = producer_queue

    def sendHello(self):
        # Send a hello message
        self.sendMessage(b"hello")

    def onOpen(self):
        # Send a hello message when the connection is opened
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the queue
        message = payload.decode('utf8')
        self.producer_queue.put(message)
        print(f"Received message: {message}")

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket closed: {reason}")

class MyWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, path):
        # Here we provide the queue when instantiating BridgeSocket
        return BridgeSocket(self.producer_queue)

if __name__ == "__main__":
    # Create a job queue
    job_queue = Queue()

    # Create WebSocket client factory with the job queue
    factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)

    # Connect the WebSocket client
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()
