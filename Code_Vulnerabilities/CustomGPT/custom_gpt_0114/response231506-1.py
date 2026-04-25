
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Process incoming messages and add to the queue
        self.producer_queue.put(payload.decode('utf8'))

    def onClose(self, wasClean, code, reason):
        print("WebSocket closed:", reason)

# Main execution
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = queue.Queue()  # Use queue.Queue for thread-safety
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function to create instances
    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

    # Example of how to process items from the queue in another thread
    import threading

    def process_queue():
        while True:
            item = job_queue.get()  # Blocks until an item is available
            print(f"Job received: {item}")
            job_queue.task_done()

    threading.Thread(target=process_queue, daemon=True).start()
