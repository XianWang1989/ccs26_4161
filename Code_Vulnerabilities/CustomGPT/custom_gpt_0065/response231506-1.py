
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
from queue import Queue  # Use the standard library queue for Python 3
import threading

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's __init__ method
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Message needs to be bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message
        self.producer_queue.put(payload.decode('utf-8'))  # Assuming UTF-8 messages

def start_reactor():
    reactor.run()

if __name__ == "__main__":
    job_queue = Queue()

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method

    threading.Thread(target=start_reactor).start()  # Start the Twisted reactor in a separate thread

    connectWS(factory)
