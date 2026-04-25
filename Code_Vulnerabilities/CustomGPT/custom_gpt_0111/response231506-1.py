
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.component import Component
from twisted.internet import reactor
import Queue  # Use `queue` for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the superclass initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process the incoming message
        self.producer_queue.put(payload)

def main():
    job_queue = Queue.Queue()  # Use queue.Queue() for Python 3
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method

    # Connect to the WebSocket server
    connectWS(factory)

    reactor.run()

if __name__ == "__main__":
    main()
