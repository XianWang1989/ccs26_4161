
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue
from twisted.internet.ssl import ClientContextFactory

# Define the BridgeSocket class
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Make sure to send byte strings

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages and put them in the job_queue
        self.producer_queue.put(payload)

# Define a factory class
class BridgeSocketFactory(WebSocketClientFactory):
    def __init__(self, url, producer_queue):
        super().__init__(url)  # Call the parent class's constructor
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        return BridgeSocket(self.producer_queue)  # Create instance of BridgeSocket

# Main function to set up connection
def main():
    job_queue = Queue()
    factory = BridgeSocketFactory("ws://localhost:7096", job_queue)
    connectWS(factory)  # This method connects the WebSocket
    reactor.run()

if __name__ == "__main__":
    main()
