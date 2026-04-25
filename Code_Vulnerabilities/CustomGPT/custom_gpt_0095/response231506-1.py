
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Important to call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()
        # You can define other logic here to handle incoming messages
        print("WebSocket connection opened.")

    def onMessage(self, payload, isBinary):
        # Put incoming messages into the queue
        self.producer_queue.put(payload.decode('utf-8'))
        print(f"Received message: {payload.decode('utf-8')}")

# Connection setup
if __name__ == '__main__':
    job_queue = Queue()  # Create a job queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a callable to instantiate the protocol
    connectWS(factory)

    # Start the Twisted reactor
    reactor.run()
