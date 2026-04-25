
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Assuming MyService is your Thrift service definition
from my_service import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

if __name__ == '__main__':
    port = 9090  # Set your desired port

    # Create a handler for your service
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use FramedTransport factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the non-blocking server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    server.serve()
