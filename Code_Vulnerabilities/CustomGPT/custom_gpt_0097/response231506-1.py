
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the base class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()
        # Add more logic here to handle incoming messages or other events

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to job queue
        self.producer_queue.put(payload.decode('utf8'))

# Usage
if __name__ == '__main__':
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory method to create instances

    # Connect to the WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()  # Start the Twisted reactor
