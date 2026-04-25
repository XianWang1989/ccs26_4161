
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        # Call the superclass initializer
        super(BridgeSocket, self).__init__()
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Ensure you're sending bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the job queue
        self.producer_queue.put(payload.decode('utf-8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed: ", reason)

def main():
    # Create a job queue
    job_queue = Queue.Queue()

    # Create the factory and pass the bridge socket with the job queue
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to return a new instance

    # Connect to the WebSocket server
    connectWS(factory)

    # Start the reactor to handle events
    reactor.run()

if __name__ == "__main__":
    main()
