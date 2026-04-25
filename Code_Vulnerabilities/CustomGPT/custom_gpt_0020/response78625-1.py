
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Make sure to import your service-generated code
from your_service_module import MyService  # replace with your actual Thrift service module

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Specify your port number
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use factory instead of transport
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server with the correct factories
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    main()
