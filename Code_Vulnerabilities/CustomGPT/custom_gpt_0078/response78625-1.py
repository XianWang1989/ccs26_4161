
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Set handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)

# Use TNonblockingTransport for non-blocking server
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the non-blocking server
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
