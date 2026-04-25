
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Ensure proper initialization of the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here you can add messages to your queue
        self.producer_queue.put(payload)
        print(f"Message received and added to queue: {payload}")

class MyWebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.protocol = lambda: BridgeSocket(producer_queue)

def main():
    job_queue = queue.Queue()
    factory = MyWebSocketClientFactory("ws://localhost:7096", job_queue)
    connectWS(factory)

    reactor.run()

if __name__ == "__main__":
    main()
