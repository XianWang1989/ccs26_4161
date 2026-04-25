
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super(BridgeSocket, self).__init__()  # Call the base class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # When a message is received, put the data in the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))

# Set up the WebSocket factory and your job queue
def main():
    job_queue = Queue.Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")

    # Assign the 'BridgeSocket' protocol to the factory
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Connect to the WebSocket
    connectWS(factory)

    # Start the Twisted reactor to listen for events
    reactor.run()

if __name__ == '__main__':
    main()
