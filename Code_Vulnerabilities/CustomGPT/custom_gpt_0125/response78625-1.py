
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from my_service import MyService  # assuming your service is defined here

class ServiceHandler:
    # Implement your service methods here
    pass

port = 9090  # Set your port number

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()  # Use TBufferedTransportFactory for non-blocking
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
