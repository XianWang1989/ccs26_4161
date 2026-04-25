
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Assuming you have a MyService and ServiceHandler defined elsewhere
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Create a non-blocking server socket
transport = TSocket.TServerSocket(port=port)  # Specify port for the server
tfactory = TTransport.TFramedTransportFactory()  # Use TFramedTransportFactory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Change this line to TNonblockingServer for non-blocking behavior
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Non-Blocking Server has started listening on port ' + str(port))
print('################################################')
server.serve()
