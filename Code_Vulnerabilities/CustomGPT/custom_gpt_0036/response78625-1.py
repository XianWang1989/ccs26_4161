
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Define your service handler class
class ServiceHandler:
    def your_method(self, args):
        # Implement your method here
        pass

# Define the port for the server
port = 9090

# Set up the handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)

# Create the transport and protocol factories
tfactory = TTransport.TFramedTransportFactory()  # Use Framed Transport Factory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')

# Serve
server.serve()
