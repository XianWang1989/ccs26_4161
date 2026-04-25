
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Assuming MyService and ServiceHandler are defined elsewhere
handler = ServiceHandler()
processor = MyService.Processor(handler)

# Set up server transport and protocol
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
