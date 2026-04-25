
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Ensure the message is bytes

    def onOpen(self):
        self.sendHello()
        # Additional logic for onOpen can be added here

# Create factory method
def create_factory(job_queue):
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances
    return factory

# Main execution
if __name__ == "__main__":
    job_queue = Queue.Queue()
    factory = create_factory(job_queue)
    connectWS(factory)
    reactor.run()
