
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Set handler to our implementation
handler = ServiceHandler()

# Create a processor for the service
processor = MyService.Processor(handler)

# Prepare server transport
transport = TSocket.TServerSocket(port=port)

# Use transport factory
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
