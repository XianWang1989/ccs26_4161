
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the parent class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for sending messages

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here, process incoming messages and put them in the queue
        self.producer_queue.put(payload)
        print("Message queued:", payload.decode())

if __name__ == '__main__':
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()

    # Set the protocol
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to the WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()
