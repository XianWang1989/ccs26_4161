
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Assuming MyService is generated Thrift code
from my_service import MyService

class ServiceHandler:
    # Implement service methods
    pass

def main():
    port = 9090  # Define your port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TNonblockingServer for non-blocking behavior
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Correct factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create and start the non-blocking server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
