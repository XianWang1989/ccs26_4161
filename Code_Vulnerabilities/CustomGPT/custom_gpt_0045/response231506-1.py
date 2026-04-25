
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Initialize the base class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Note: Message should be bytes

    def onOpen(self):
        self.sendHello()
        # You can now add logic here to handle incoming messages
        # e.g., self.producer_queue.put(data)

def start_client():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    reactor.connectTCP("localhost", 7096, factory)

if __name__ == "__main__":
    start_client()
    reactor.run()
