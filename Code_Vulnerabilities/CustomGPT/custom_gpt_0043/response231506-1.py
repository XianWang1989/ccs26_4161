
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from twisted.internet import reactor
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Important to call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Make sure to send bytes, not string

    def onOpen(self):
        # Sending a message as soon as the websocket opens
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Example to put incoming data onto the queue
        if not isBinary:
            # Assuming messages are UTF-8 encoded strings
            message = payload.decode('utf8')
            self.producer_queue.put(message)  # Put message into the queue
            print(f"Received message: {message}")

class MyWebSocketClientFactory(WebSocketClientFactory):
    protocol = BridgeSocket  # Set the protocol class here

    def __init__(self, *args, **kwargs):
        producer_queue = kwargs.pop('producer_queue', None)
        super().__init__(*args, **kwargs)
        self.producer_queue = producer_queue

    def buildProtocol(self, addr):
        # Return an instance of BridgeSocket with the shared queue
        return self.protocol(self.producer_queue)

if __name__ == "__main__":
    job_queue = Queue()  # Create the shared job queue
    factory = MyWebSocketClientFactory("ws://localhost:7096", producer_queue=job_queue)

    # Connect the WebSocket
    from autobahn.twisted.websocket import connectWS
    connectWS(factory)

    reactor.run()
