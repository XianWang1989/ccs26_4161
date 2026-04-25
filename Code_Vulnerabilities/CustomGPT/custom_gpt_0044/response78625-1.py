
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Replace with your actual service module

class ServiceHandler:
    # Your service implementation here
    pass

def main():
    port = 9090

    # Create a handler for your service
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TBufferedTransport or TFramedTransport
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create the non-blocking server
    server = TServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
