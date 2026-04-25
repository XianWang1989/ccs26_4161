
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated Thrift code
from your_service import MyService

class ServiceHandler:
    def your_method(self, params):
        # Your service implementation here
        return "response"

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set transport and protocol
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TFramedTransport.Factory()
pfactory = TBinaryProtocol.TBinaryProtocol.Factory()

# Set up the non-blocking server
server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print("Python Server has started listening on port 9090")
try:
    server.serve()
except Exception as e:
    print(f"Server encountered an error: {e}")
