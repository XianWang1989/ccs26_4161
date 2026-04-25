
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
from my_service import MyService  # Import your generated Thrift service

class ServiceHandler:
    def my_method(self):
        # Implement your service method
        return "Hello, Thrift!"

if __name__ == "__main__":
    port = 9090  # Specify your port number

    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create non-blocking transport and protocol
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()  # Use TBufferedTransport for non-blocking
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create non-blocking server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    server.serve()
