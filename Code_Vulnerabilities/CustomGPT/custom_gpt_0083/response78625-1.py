
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Assuming MyService and ServiceHandler are correctly defined elsewhere

# Set handler to our implementation
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)

# Use TTransportFactory instead of TFramedTransport directly
tfactory = TTransport.TTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
