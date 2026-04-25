
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
from your_thrift_module import MyService  # Replace with your actual thrift module

class ServiceHandler:
    def your_method(self, ...) :
        # Implementation of your service methods
        pass

def main():
    port = 9090  # Define your port

    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use the factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the non-blocking server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    main()
