
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Adjust according to your service

class ServiceHandler:
    # Implement your service methods here
    def your_method(self):
        pass

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set transport and protocol
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TFramedTransport.Factory()  # Note the use of Factory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port 9090')
print('################################################')
server.serve()
