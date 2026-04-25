
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from thrift.protocol import TBinaryProtocol

# Assuming MyService and ServiceHandler are defined properly
class ServiceHandler:
    def my_method(self):
        # Implementation of your service method
        pass

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Create a non-blocking server
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TFramedTransportFactory()  # Use TFramedTransportFactory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port 9090')
print('################################################')
server.serve()
