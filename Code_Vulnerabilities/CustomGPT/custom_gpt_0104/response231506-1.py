
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        # Call the parent class initializer
        super(BridgeSocket, self).__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()
        # Add additional onOpen functionality as needed

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket closed: {reason}")

# Setup and run the WebSocket client
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = Queue()

    # Here we create a new instance of BridgeSocket with job_queue.
    factory.protocol = lambda: BridgeSocket(job_queue)

    connectWS(factory)
    reactor.run()
