
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service_module import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()  # Use framed transport factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up a non-blocking server
    server = TServer.TNonblockingServer(
        processor, transport, tfactory, pfactory
    )

    print('Python Server has started listening on port 9090')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
