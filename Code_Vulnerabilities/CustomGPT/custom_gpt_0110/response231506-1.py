
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue  # Use standard library Queue
import json

# A class extending WebSocketClientProtocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(json.dumps({"message": "hello"}).encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the job queue
        self.producer_queue.put(payload.decode('utf8'))

# Factory to manage WebSocket connections
class MyWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.protocol = lambda: BridgeSocket(producer_queue)

# Main connection code
if __name__ == "__main__":
    job_queue = Queue()
    factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)
    reactor.run()
