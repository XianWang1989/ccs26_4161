
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your service and handler implementation
from your_service_package import MyService  # Adjust the path as needed

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Define your port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use a non-blocking transport
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()  # Use TBufferedTransport for compatibility
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create the non-blocking server
    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    main()
