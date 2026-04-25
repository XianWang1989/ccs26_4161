
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import Queue  # or from queue import Queue in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Ensure the base class is initialized
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure the message is sent as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload)
        print("Message received and added to queue:", payload)

def start_client():
    job_queue = Queue.Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create a new instance
    connectWS(factory)

if __name__ == '__main__':
    start_client()
    reactor.run()
