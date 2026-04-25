
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Example service handler
class ServiceHandler:
    def ping(self):
        return "pong"

# Assuming MyService is already defined and generated from your Thrift IDL
processor = MyService.Processor(ServiceHandler())

# Define the transport and protocol factories
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TFramedTransportFactory()  # Use the factory instead of instance
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Create the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port 9090')
print('################################################')
server.serve()
