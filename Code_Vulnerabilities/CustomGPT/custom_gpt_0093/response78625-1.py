
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Set handler to our implementation
handler = ServiceHandler()

processor = MyService.Processor(handler)

# Create a server socket that listens on the specified port
transport = TSocket.TServerSocket(port=port)

# Use TTransport.TBufferedTransport for the server
tfactory = TTransport.TBufferedTransportFactory()  
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Set up the server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
