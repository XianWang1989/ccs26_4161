
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the job queue
        self.producer_queue.put(payload.decode('utf8'))

class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket

# Example usage
if __name__ == "__main__":
    job_queue = queue.Queue()
    factory = MyWebSocketClientFactory("ws://localhost:7096")

    # Use a lambda function to pass the queue to the protocol
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)
    reactor.run()
