
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Set handler to our implementation
handler = ServiceHandler()  # Ensure ServiceHandler is defined
processor = MyService.Processor(handler)

# Create server transport
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use FramedTransportFactory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
