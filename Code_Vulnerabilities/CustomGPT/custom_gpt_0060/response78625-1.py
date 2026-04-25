
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer

# Assume MyService is already defined elsewhere
class ServiceHandler:
    # Implement your service methods here
    pass

if __name__ == '__main__':
    port = 9090  # Specify the port

    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Set up a server socket
    transport = TSocket.TServerSocket(port=port)

    # Use TFramedTransportFactory instead of TFramedTransport
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
