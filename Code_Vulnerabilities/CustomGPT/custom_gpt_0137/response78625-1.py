
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Your service handler and service definitions go here
from your_service_module import MyService  # Import your Thrift-generated service classes

class ServiceHandler:
    # Implement your service methods as per your Thrift IDL
    pass

port = 9090  # Choose your port

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Use TSocket for the server socket
transport = TSocket.TServerSocket(port=port)

# Use TTransport.TBufferedTransport for compatibility
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
