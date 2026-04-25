
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
import queue

# Custom WebSocket Client Protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Properly initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Assuming the incoming data needs to be processed or added to the queue
        self.producer_queue.put(payload)

# Custom WebSocket Client Factory
class BridgeFactory(WebSocketClientFactory):
    protocol = BridgeSocket

def start_websocket():
    job_queue = queue.Queue()
    factory = BridgeFactory("ws://localhost:7096")

    # Set the job queue to the protocol instance
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    start_websocket()
