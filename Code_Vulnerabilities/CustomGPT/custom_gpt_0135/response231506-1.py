
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def onOpen(self):
        self.sendHello()

    def sendHello(self):
        self.sendMessage(b"hello")

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to queue
        self.producer_queue.put(payload.decode('utf-8'))

class BridgeWebSocketFactory(WebSocketClientFactory):
    protocol = BridgeSocket

def main():
    job_queue = Queue()
    factory = BridgeWebSocketFactory("ws://localhost:7096")  # Your WebSocket URL
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to pass the queue

    # Connect to the WebSocket
    connectWS(factory)
    # Start the Twisted reactor to handle events
    reactor.run()

if __name__ == "__main__":
    main()
