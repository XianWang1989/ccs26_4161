
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol
from autobahn.twisted.util import connectWS
import queue  # Use `queue` for Python 3.x

# Create a job queue
job_queue = queue.Queue()

# Create WebSocket client factory
factory = WebSocketClientFactory("ws://localhost:7096")
factory.protocol = lambda: BridgeSocket(job_queue)  # Use a factory function

# Connect to the WebSocket server
connectWS(factory)
