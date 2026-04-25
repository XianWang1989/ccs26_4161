
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import Deferred
import Queue  # For Python 2, use 'queue' for Python 3


class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def onOpen(self):
        self.sendHello()

    def sendHello(self):
        self.sendMessage(b"hello")

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to queue
        self.producer_queue.put(payload)
        print("Received and queued:", payload)


def main():
    job_queue = Queue.Queue()  # Use 'queue.Queue()' for Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Create a new instance of BridgeSocket
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == '__main__':
    main()
