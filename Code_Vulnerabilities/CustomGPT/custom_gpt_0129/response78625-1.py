
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from thrift.server import TServer
from your_service import MyService  # Import your service definitions

class ServiceHandler:
    # Implement your service methods here
    pass

if __name__ == "__main__":
    # Set handler to our implementation
    handler = ServiceHandler()

    # Processor
    processor = MyService.Processor(handler)

    # Use TSocket and TFramedTransport properly
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(transport.getPort()))
    print('################################################')

    # Starting the server
    server.serve()
