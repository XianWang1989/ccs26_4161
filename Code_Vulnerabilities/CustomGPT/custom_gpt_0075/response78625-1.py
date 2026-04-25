
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class ServiceHandler:
    def some_function(self):
        # Your implementation
        pass

port = 9090  # Example port

# Set handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Corrected factory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
