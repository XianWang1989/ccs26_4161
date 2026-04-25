
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.transport import TNonblockingServer

# Import your service handler and service definition
from your_service_module import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090
    # set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TTransport.TFramedTransport for non-blocking
    tfactory = TTransport.TFramedTransportFactory()

    # Use TBinaryProtocol, suitable for TFramedTransport
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # set server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Non-blocking Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    main()
