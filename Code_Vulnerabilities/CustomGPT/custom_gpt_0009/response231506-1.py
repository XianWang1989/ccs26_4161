
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
import Queue  # Use queue in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent class's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()
        # Add additional handling for incoming data, e.g., onMessage

def main():
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = Queue.Queue()  # Use queue.Queue() for Python 3
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances
    connectWS(factory)

    reactor.run()

if __name__ == '__main__':
    main()
