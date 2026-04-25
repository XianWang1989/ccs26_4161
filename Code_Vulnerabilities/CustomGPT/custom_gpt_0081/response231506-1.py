
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
import Queue  # In Python 2.x, use Queue; in Python 3.x, use queue
import twisted.reactor

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # WebSocket sendMessage expects bytes.

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # You can add the received message to the job queue
        self.producer_queue.put(payload)
        print("Message received and added to queue:", payload)

def main():
    job_queue = Queue.Queue()  # Create a job queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Assign a factory for instantiation

    connectWS(factory)
    twisted.reactor.run()

if __name__ == '__main__':
    main()
