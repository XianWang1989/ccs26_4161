
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer  # Import server classes

# Define your service handler
class ServiceHandler:
    def your_method(self):
        # Implement your service logic here
        pass

# Create and configure the server
handler = ServiceHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TFramedTransportFactory()  # Use the framed transport factory
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Use a thread pool server for non-blocking
server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print('Python Server has started listening on port ' + str(port))
print('################################################')
server.serve()
