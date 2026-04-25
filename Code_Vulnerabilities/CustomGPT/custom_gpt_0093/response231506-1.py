
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from queue import Queue
from autobahn.twisted.util import encode

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(encode("hello"))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Enqueue incoming messages
        self.producer_queue.put(payload.decode('utf8'))

def main():
    job_queue = Queue()  # Initialize the queue
    factory = WebSocketClientFactory("ws://localhost:7096")  # Create the factory

    # Create a protocol factory that creates BridgeSocket instances
    class MyProtocolFactory(WebSocketClientFactory):
        def buildProtocol(self, addr):
            return BridgeSocket(job_queue)  # Pass the queue to the protocol

    factory.protocol = MyProtocolFactory

    # Connect to the WebSocket server
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()  # Start the Twisted reactor

if __name__ == "__main__":
    main()
