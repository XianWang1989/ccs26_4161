
from thrift import Thrift
from thrift.transport import TServer, TSocket, TTransport
from thrift.protocol import TBinaryProtocol

# set handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use the Factory here
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
