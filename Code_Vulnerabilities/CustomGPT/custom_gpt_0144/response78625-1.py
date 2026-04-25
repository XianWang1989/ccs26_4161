from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_service import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

# set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Use the TSocket for the transport layer
transport = TSocket.TServerSocket(port=port)

# Use the default transport type, which is TBufferedTransport or you can choose TFramedTransport
tfactory = TTransport.TBufferedTransportFactory()  # Default transport
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print 'Python Server has started listening on port ' + str(port)
print '################################################'

# This starts the server to listen and handle requests.
server.serve()
