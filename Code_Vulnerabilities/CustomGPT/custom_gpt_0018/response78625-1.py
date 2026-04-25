
from thrift import TProcessor
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from thrift.protocol import TBinaryProtocol

# Assume MyService and ServiceHandler are defined elsewhere

port = 9090  # Replace with your desired port

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Use TNonblockingServer for non-blocking behavior
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransport.Factory()  # Use Factory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
