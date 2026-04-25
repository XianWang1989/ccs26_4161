
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from your_service import MyService  # Replace with your actual service

class ServiceHandler:
    # Implement your service methods here
    pass

port = 9090  # Specify your port

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)

# Use TTransport.TFramedTransportFactory for proper transport creation
tfactory = TTransport.TFramedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
