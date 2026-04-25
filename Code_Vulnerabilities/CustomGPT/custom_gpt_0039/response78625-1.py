
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_module import MyService  # Make sure to import your generated Thrift classes

class ServiceHandler:
    # Your service implementation here
    pass

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set up server with proper transport and protocol
transport = TSocket.TServerSocket(port=port)

# Using TTransport.TFramedTransport as both input and output transport
tfactory = TTransport.TFramedTransport.Factory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
