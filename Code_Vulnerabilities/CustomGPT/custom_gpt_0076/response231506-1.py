
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import set_debug_logger
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure proper initialization of WebSocketClientProtocol
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you send bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and put them in the queue
        if not isBinary:
            message = payload.decode('utf8')
            self.producer_queue.put(message)

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed:", reason)

# Using the WebSocketClientFactory
def start_client():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory pattern
    set_debug_logger()  # Enable logging (optional)
    connectWS(factory)

if __name__ == '__main__':
    start_client()
    reactor.run()
