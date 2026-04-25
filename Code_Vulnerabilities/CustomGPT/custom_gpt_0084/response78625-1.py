
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service_module import MyService  # Replace with actual service module

class ServiceHandler:
    def your_method(self):
        # Implementation of your method
        pass

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket for handling connections
    transport = TSocket.TServerSocket(port=9090)

    # Framed transport for non-blocking
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create server with multi-threaded support
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
