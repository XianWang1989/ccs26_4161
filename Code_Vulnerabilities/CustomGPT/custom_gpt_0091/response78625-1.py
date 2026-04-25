
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Use TServerSocket for the transport
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use a factory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print(f'Python Server has started listening on port {port}')
print('################################################')
server.serve()
