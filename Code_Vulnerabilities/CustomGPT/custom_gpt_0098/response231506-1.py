
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()
        # You can add more handling logic here

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and fill the queue
        self.producer_queue.put(payload.decode('utf8'))
        print(f"Message received and added to queue: {payload.decode('utf8')}")

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed:", reason)

class CustomWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Directly set the protocol class

    def __init__(self, *args, **kwargs):
        self.producer_queue = kwargs.pop('producer_queue', None)
        super().__init__(*args, **kwargs)

    def buildProtocol(self, url):
        return self.protocol(self.producer_queue)

if __name__ == "__main__":
    job_queue = Queue()
    factory = CustomWebSocketClientFactory("ws://localhost:7096", producer_queue=job_queue)
    connectWS(factory)

    reactor.run()
