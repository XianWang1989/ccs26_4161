
class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Initialize the base class
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Send message as bytes

    def onOpen(self):
        self.sendHello()
        # Example of adding to the job queue
        self.producer_queue.put("Job added on open")

    def onMessage(self, payload, isBinary):
        # Handle incoming messages
        self.producer_queue.put(payload.decode('utf8'))  # Add incoming message to queue
