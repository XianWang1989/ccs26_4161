
from thrift import Thrift
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

# Import your service
from your_service import MyService  # Replace with your actual service

class ServiceHandler:
    def your_method(self, args):
        # Implement your service method here
        return "Response"

def main():
    port = 9090

    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create a non-blocking server
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use the Factory class
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    # Start the server
    server.serve()

if __name__ == '__main__':
    main()
