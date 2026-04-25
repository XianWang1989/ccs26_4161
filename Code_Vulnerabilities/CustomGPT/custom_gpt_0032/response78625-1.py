
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from my_service import MyService  # replace with your actual service module

# Set handler to your implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set up transport
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()  # Use buffered transport
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
