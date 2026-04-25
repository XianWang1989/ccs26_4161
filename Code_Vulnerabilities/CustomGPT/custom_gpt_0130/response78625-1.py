
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Your service implementation
class ServiceHandler:
    # Implement your service methods here
    pass

port = 9090  # Set your desired port

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Create transport and protocol factories
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransport.Factory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the non-blocking server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
