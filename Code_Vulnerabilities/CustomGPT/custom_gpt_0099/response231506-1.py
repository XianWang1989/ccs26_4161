
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
from twisted.internet import reactor
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for sending messages

    def onOpen(self):
        self.sendHello()
        # Additional code to handle incoming data
        # You could add logic to fill the job queue with incoming messages here

def start_websocket():
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = Queue.Queue()
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function
    connectWS(factory)

if __name__ == "__main__":
    start_websocket()
    reactor.run()  # Start the Twisted reactor
