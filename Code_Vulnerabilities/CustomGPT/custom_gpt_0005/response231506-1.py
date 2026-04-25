
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from twisted.internet import reactor
import queue

class BridgeSocket(WebSocketClientProtocol):
    def __init__(self, producer_queue):
        super().__init__()  # Call the parent constructor
        self.producer_queue = producer_queue

    def sendHello(self):
        self.sendMessage(b"hello")  # Use bytes for messages

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        # Handle incoming messages
        self.producer_queue.put(payload.decode('utf-8'))  # Add incoming data to the queue

def on_message_received(job_queue):
    while True:
        message = job_queue.get()  # Get messages from the queue
        print(f"Received: {message}")
        job_queue.task_done()

if __name__ == '__main__':
    job_queue = queue.Queue()

    factory = WebSocketClientFactory("ws://localhost:7096")
    factory.protocol = lambda: BridgeSocket(job_queue)

    # Start the WebSocket connection
    connectWS(factory)

    # Start a thread to process the queue
    import threading
    threading.Thread(target=on_message_received, args=(job_queue,), daemon=True).start()

    # Start the Twisted reactor
    reactor.run()
