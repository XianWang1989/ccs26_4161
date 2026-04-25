
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted import connectWS
from twisted.internet import reactor
import Queue  # For Python 2.x, use `from queue import Queue` for Python 3.x

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call to the parent class's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming message and add to the queue
        self.producer_queue.put(payload.decode('utf8'))  # Adjust as needed

def onConnect(factory):
    print("WebSocket connection open")

def main():
    job_queue = Queue.Queue()  # or use `from queue import Queue` for Python 3.x
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Set the protocol factory
    factory.protocol = lambda: BridgeSocket(job_queue)

    factory.onOpen = onConnect  # Set the open callback

    connectWS(factory)
    reactor.run()

if __name__ == '__main__':
    main()
