
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import sleep
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's __init__ method
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure the message is bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Put incoming messages on the queue
        self.producer_queue.put(payload.decode('utf-8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed")

# Function to create the WebSocket client
def run_client():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create a new instance
    connectWS(factory)

if __name__ == '__main__':
    run_client()
    reactor.run()
