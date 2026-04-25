
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Adjust import based on your service

class ServiceHandler:
    # Implement your service methods
    def your_method(self, param):
        return "Response"

handler = ServiceHandler()
processor = MyService.Processor(handler)

# Use TServerSocket for transport
transport = TSocket.TServerSocket(port=port)

# Use a framed transport factory
tfactory = TTransport.TFramedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the threaded server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
