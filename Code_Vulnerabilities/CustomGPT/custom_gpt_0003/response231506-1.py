
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
import queue  # Use queue from the standard library
import threading

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the superclass's constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Messages must be bytes

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Here, you can process incoming messages and add them to the queue
        self.producer_queue.put(payload)

# Main code to connect
job_queue = queue.Queue()  # Create a thread-safe job queue
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory to create instances

connectWS(factory)

# To process the queue in a different thread, you can do:
def process_queue():
    while True:
        job = job_queue.get()
        # Process the job
        print(f"Processing job: {job}")
        job_queue.task_done()

# Start a thread to process the queue
threading.Thread(target=process_queue, daemon=True).start()
