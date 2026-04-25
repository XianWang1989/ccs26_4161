
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Make sure to import your service
# from your_service_module import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create a transport factory for framed transport
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransport.Factory()  # Use factory here
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
