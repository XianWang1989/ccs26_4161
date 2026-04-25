
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated Thrift code here
from your_thrift_module import MyService

class ServiceHandler:
    def ping(self):
        return "pong"

# Set up the server
port = 9090  # Your chosen port
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()  # Changed to TBufferedTransportFactory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
