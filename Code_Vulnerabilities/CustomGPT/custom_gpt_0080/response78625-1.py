
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from thrift.server import TServer

# Assuming MyService and ServiceHandler are already defined
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set up the transport and protocol factories
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Changed this line
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
