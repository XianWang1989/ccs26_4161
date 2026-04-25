
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# set handler to your implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use factory instead of instance
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
