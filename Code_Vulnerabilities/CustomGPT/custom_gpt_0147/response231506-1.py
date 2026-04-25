
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue  # Use `queue.Queue` in Python 3, `Queue.Queue` in Python 2

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here, you can put incoming data into the producer queue
        self.producer_queue.put(payload.decode('utf8'))

def main():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda function to create a new instance

    # You can now interact with `job_queue` in your main thread or other threads

    # Start the Twisted reactor
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

if __name__ == "__main__":
    main()
