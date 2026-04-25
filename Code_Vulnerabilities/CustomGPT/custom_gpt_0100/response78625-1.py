
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Set handler to your implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Use TServerSocket for transport
transport = TSocket.TServerSocket(port=port)

# Use TTransport.TBufferedTransport or TTransport.TFramedTransport
tfactory = TTransport.TBufferedTransportFactory()  # Changed to TBufferedTransport
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
