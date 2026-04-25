
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Assuming ServiceHandler and MyService are already defined
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Create a non-blocking server socket
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the non-blocking server
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
