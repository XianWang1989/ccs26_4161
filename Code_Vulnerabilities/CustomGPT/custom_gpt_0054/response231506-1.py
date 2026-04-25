
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
import Queue  # Python 2.x, use `from queue import Queue` for Python 3.x

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, *args, **kwargs):
        super(BridgeSocket, self).__init__(*args, **kwargs)
        self.producer_queue = kwargs.get('producer_queue')

    def sendHello(self):
        self.sendMessage(b"hello")  # Remember to send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # You can use the producer_queue here to add incoming messages
        self.producer_queue.put(payload)
        # Process the message or handle it as needed

if __name__ == "__main__":
    # Create a job queue
    job_queue = Queue.Queue()

    # Create a factory and assign the BridgeSocket class
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda *args, **kwargs: BridgeSocket(*args, producer_queue=job_queue, **kwargs)

    # Connect WebSocket
    connectWS(factory)
