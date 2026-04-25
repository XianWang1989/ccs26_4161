from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS
from twisted.internet import reactor
import queue  # or import Queue if using Python 2

# Your protocol class
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self):
        super(BridgeSocket, self).__init__()
        self.producer_queue = None

    def sendHello(self):
        self.sendMessage(b"hello")  # sendMessage expects bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        self.producer_queue.put(payload)

# Custom factory to pass queue
class BridgeFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super(BridgeFactory, self).__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        proto = BridgeSocket()
        proto.producer_queue = self.producer_queue
        return proto

# Usage
job_queue = queue.Queue()
factory = BridgeFactory("ws://localhost:7096", job_queue)
connectWS(factory)

reactor.run()
