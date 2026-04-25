
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

# Import your generated Thrift classes
from your_thrift_module import MyService

class ServiceHandler:
    def ping(self):
        return "pong"

    # Define other methods as per your service

if __name__ == "__main__":
    port = 9090

    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create server transport
    transport = TSocket.TServerSocket(port=port)

    # Create transport and protocol factories
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    # Start the server
    server.serve()
