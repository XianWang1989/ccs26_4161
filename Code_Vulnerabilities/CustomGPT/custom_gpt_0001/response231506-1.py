
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Make sure to encode the string

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and add them to the queue
        self.producer_queue.put(payload.decode('utf8'))  # Decode incoming message

def create_bridge_socket(factory, job_queue):
    return BridgeSocket(job_queue)

if __name__ == '__main__':
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    # Assign the factory’s protocol to be a lambda that creates BridgeSocket instances
    factory.protocol = lambda: create_bridge_socket(factory, job_queue)

    connectWS(factory)
    reactor.run()
