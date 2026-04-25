
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from queue import Queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent class initializer
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage("hello".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Add incoming messages to the job queue
        self.producer_queue.put(payload.decode('utf8'))

# Connection code
if __name__ == "__main__":
    job_queue = Queue()
    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function to instantiate

    reactor.connectTCP("localhost", 7096, factory)
    reactor.run()

# Example of how to process items from the queue
def process_queue():
    while True:
        job = job_queue.get()
        print(f"Processed job: {job}")
        job_queue.task_done()

# Start a thread to process the job queue
import threading
threading.Thread(target=process_queue, daemon=True).start()
