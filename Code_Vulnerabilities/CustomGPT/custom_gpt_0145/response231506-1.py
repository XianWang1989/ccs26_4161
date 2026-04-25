
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.websocket import connectWS
import queue  # Python 3's queue module

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))  # Encode the message before sending

    def onOpen(self):
        self.sendHello()
        # Additional handling for when the socket is opened

def create_connection():
    job_queue = queue.Queue()  # Create a job queue
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Set a factory method to instantiate the protocol with the queue
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect using the factory
    connectWS(factory)

# Call the function to create the connection
create_connection()
