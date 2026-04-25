
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from thrift.server import TNonblockingServer

# Assume MyService and ServiceHandler are already defined
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set transport and protocol factories
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TFramedTransportFactory()  # Note the correct factory usage
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Create a non-blocking server
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port 9090')
print('################################################')
server.serve()
