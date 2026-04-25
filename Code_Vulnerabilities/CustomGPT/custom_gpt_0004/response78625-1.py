
from thrift.transport import TTransport, TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Import your service definition

class ServiceHandler:
    # Implement your service methods here
    def your_method(self):
        return "Hello, World!"

if __name__ == "__main__":
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Set up the transport
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create the server with non-blocking support
    server = TServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')

    # Serve the server
    server.serve()
