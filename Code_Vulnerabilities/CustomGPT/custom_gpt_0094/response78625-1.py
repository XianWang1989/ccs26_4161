
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer  # Change to non-blocking server
from your_service import MyService  # Replace with your actual service module

class ServiceHandler:
    def your_method(self, arg):
        # Your implementation here
        return "Response"

if __name__ == "__main__":
    port = 9090  # Specify your port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Transport and protocol setup
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use FramedTransportFactory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up non-blocking server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
