
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload.decode('utf8'))
        print("Message received and added to queue:", payload)

class MyFactory(WebSocketClientFactory):
    protocol = BridgeSocket

    def __init__(self, url, job_queue):
        super(MyFactory, self).__init__(url)
        self.job_queue = job_queue

    def buildProtocol(self, addr):
        return self.protocol(self.job_queue)

# Main code to create a job queue and connect to the WebSocket server
if __name__ == '__main__':
    job_queue = Queue.Queue()
    factory = MyFactory("ws://localhost:7096", job_queue)

    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()
