
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue  # Use "from queue import Queue" for Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Don't forget to call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Make sure to encode the message

    def onOpen(self):
        self.sendHello()

class CustomWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        # Here we instantiate the BridgeSocket with the job queue
        return BridgeSocket(self.producer_queue)

# In your main function or entry point
if __name__ == '__main__':
    job_queue = Queue()

    factory = CustomWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)

    reactor.run()
