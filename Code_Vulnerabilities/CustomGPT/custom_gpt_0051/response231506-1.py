
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.util import connectWS
from twisted.internet import reactor
import Queue  # For Python 2.x, use 'import queue' for Python 3.x

# Define your WebSocket client protocol
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for the message

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here you can handle incoming messages
        message = payload.decode('utf8')  # Decode if needed
        self.producer_queue.put(message)  # Add incoming data to the queue

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))

# Create an instance of the WebSocket client factory
class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket

# Connect to WebSocket
def main():
    job_queue = Queue.Queue()  # Use 'queue.Queue()' for Python 3.x
    factory = MyWebSocketClientFactory("ws://localhost:7096")  # Use your WebSocket URL
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to instantiate the protocol
    connectWS(factory)
    reactor.run()  # Start the Twisted reactor

if __name__ == "__main__":
    main()
