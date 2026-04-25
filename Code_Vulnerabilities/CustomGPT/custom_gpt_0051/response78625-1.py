
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Create a transport socket
transport = TSocket.TServerSocket(port=port)

# Use TTransport.TBufferedTransport instead of TFramedTransport for the input transport factory
tfactory = TTransport.TBufferedTransportFactory()

# Using TBinaryProtocol
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
