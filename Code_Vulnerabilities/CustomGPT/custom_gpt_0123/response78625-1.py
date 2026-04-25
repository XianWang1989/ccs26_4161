
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Example Service Handler
class ServiceHandler:
    def your_service_method(self, args):
        # Implement your service logic here
        pass

# Set up the server
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)

# Use TBufferedTransport for the server
tfactory = TTransport.TBufferedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
