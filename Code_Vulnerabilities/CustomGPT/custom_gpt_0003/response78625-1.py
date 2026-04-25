
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your service specific classes here (e.g. MyService)

class ServiceHandler:
    # Implementation of your service methods
    def your_service_method(self, param):
        # Your service logic here
        pass

port = 9090  # Your chosen port

# Set the handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Correct factory instantiation
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
