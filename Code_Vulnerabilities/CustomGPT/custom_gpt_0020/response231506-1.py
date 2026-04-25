
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
import Queue  # Use `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the job queue
        self.producer_queue.put(payload)  # Assuming payload is directly usable
        # Do further processing as needed

def main():
    job_queue = Queue.Queue()  # Use `queue.Queue()` if you're using Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a callable to create the protocol instance

    from twisted.internet import reactor
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == '__main__':
    main()
