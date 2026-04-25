
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import Queue  # Use 'queue' in Python 3
import json

# Your WebSocket Protocol Class
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send as bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the job queue
        message = json.loads(payload)
        self.producer_queue.put(message)

# Custom factory to override buildProtocol
class BridgeSocketFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super(BridgeSocketFactory, self).__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        return BridgeSocket(self.producer_queue)  # Pass the queue here

# Main connection code
if __name__ == "__main__":
    job_queue = Queue.Queue()  # Use 'queue.Queue()' for Python 3
    factory = BridgeSocketFactory("ws://localhost:7096", job_queue)

    # Connect WebSocket
    connectWS(factory)
    reactor.run()
