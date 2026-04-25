
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Define your handler here
class ServiceHandler:
    def your_method(self, args):
        # Implement your service logic here
        return "Response"

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use TFramedTransportFactory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
