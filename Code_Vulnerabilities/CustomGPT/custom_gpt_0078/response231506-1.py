
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        self.producer_queue = producer_queue
        super().__init__()  # Call the superclass constructor

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf-8'))

def main():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Instantiate the protocol, passing the job queue
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to the WebSocket server
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    main()
