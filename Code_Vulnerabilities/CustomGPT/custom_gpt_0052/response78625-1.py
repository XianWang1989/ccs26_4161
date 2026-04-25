
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from thrift.server import TNonblockingServer

# Import your generated Thrift code
from your_service import MyService

class ServiceHandler:
    # Implement your service methods here
    def your_method(self, param):
        return "Result"

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create transport
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransport.Factory()  # Use the factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Use TNonblockingServer for non-blocking behavior
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')

    # Start the server
    server.serve()

if __name__ == "__main__":
    main()
