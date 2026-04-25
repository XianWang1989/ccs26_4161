
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
import Queue  # Use `queue` in Python 3
import threading

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Note the byte string

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        self.producer_queue.put(payload)  # Fill the queue with incoming data

def start_websocket(queue):
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(queue)  # Use a lambda to create an instance
    connectWS(factory)

if __name__ == "__main__":
    job_queue = Queue.Queue()  # For Python 3, use `queue.Queue()`
    threading.Thread(target=start_websocket, args=(job_queue,)).start()
