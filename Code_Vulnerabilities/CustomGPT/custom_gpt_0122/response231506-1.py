
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure to call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket closed: {reason}")

if __name__ == "__main__":
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create a new instance

    # Connect to the WebSocket server
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()
