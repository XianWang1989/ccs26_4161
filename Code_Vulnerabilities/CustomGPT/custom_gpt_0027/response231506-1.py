
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue  # Use 'queue' instead of 'Queue' for Python 3

class BridgeSocket(WebSocketClientProtocol):

    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Assuming you want to add messages to the queue
        self.producer_queue.put(payload)  # Add incoming data to the queue

def main():
    job_queue = queue.Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method

    connectWS(factory)  # Remember to call connectWS correctly

    reactor.run()  # Start the Twisted reactor

if __name__ == "__main__":
    main()
