
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add them to the job queue
        self.producer_queue.put(payload.decode('utf8'))

class BridgeSocketFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        # Create an instance of your protocol with the queue
        return BridgeSocket(self.producer_queue)

# Example usage
if __name__ == '__main__':
    job_queue = Queue()
    factory = BridgeSocketFactory("ws://localhost:7096", job_queue)
    connectWS(factory)
    reactor.run()
