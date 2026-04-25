
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):

    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # You can process incoming messages and add to the queue here
        self.producer_queue.put(payload.decode('utf-8'))

class MyWebSocketClientFactory(WebSocketClientFactory):

    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        return BridgeSocket(self.producer_queue)

if __name__ == '__main__':
    job_queue = Queue()
    factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)
    reactor.run()
