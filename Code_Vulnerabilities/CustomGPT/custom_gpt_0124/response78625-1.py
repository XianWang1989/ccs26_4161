
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
from myservice import MyService  # Import your Thrift-generated service

class ServiceHandler:
    # Implement your service methods here
    pass

# Set up handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server using TNonblockingServer for non-blocking behavior
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
