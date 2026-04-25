
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
from your_service import MyService  # Ensure to import your generated service

class ServiceHandler:
    # Implement your service methods here
    pass

if __name__ == "__main__":
    port = 9090  # Define your port

    # Set handler to our implementation
    handler = ServiceHandler()

    # Create processor and transport
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use a factory instead of a transport
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
