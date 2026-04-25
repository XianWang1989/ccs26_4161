
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call parent initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Message must be bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add the incoming message to the queue
        self.producer_queue.put(payload.decode('utf-8'))

# Custom factory to instantiate BridgeSocket with a queue
class BridgeSocketFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, *args, **kwargs):
        return BridgeSocket(self.producer_queue)

if __name__ == '__main__':
    job_queue = Queue()
    factory = BridgeSocketFactory("ws://localhost:7096", job_queue)
    connectWS(factory)
    reactor.run()
