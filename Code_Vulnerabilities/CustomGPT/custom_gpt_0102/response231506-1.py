
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
import queue  # Use `queue` in Python 3

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Ensure proper initialization
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode the message

    def onOpen(self):
        self.sendHello()
        # Add logic to handle incoming data and fill the queue

# Example usage
if __name__ == "__main__":
    from twisted.internet import reactor

    job_queue = queue.Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Customize the factory to use the BridgeSocket with the job queue
    def create_protocol():
        return BridgeSocket(job_queue)

    factory.protocol = create_protocol  # Assign a callable here
    connectWS(factory)

    reactor.run()
