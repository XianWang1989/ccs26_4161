
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure you call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf8'))

# Usage
if __name__ == "__main__":
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Create an instance of BridgeSocket with the job_queue
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create the instance

    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()
