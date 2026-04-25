
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Assume MyService is already defined and includes MyService.Processor
class ServiceHandler:
    # Implementation of your service methods

# Initialize handler and create a processor
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Create the socket and transport factories
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use FramedTransportFactory here
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
