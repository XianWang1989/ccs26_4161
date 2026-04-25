
from thrift import TTransport, TServer, TBinaryProtocol
from thrift.transport import TSocket
from thrift.server import TNonblockingServer

# Define your ServiceHandler here
class ServiceHandler:
    # Implement your service methods
    pass

handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server to be non-blocking
server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
