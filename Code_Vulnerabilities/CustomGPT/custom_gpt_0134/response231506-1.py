
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onConnect(self, response):
        print("WebSocket connection established:", response.peer)

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the queue
        self.producer_queue.put(payload.decode('utf-8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed:", reason)

# Connection code
def main():
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create a new instance
    connectWS(factory)
    reactor.run()

if __name__ == "__main__":
    main()
