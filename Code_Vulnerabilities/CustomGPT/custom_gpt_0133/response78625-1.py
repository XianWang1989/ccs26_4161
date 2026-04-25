
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import MyService  # Import your generated service

class ServiceHandler:
    def my_method(self):
        # Your service implementation goes here
        return "Hello, Thrift!"

if __name__ == '__main__':
    # Set up the handler and processor
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket and TFramedTransport
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransport.Factory()  # Use Factory instead of instance
    pfactory = TBinaryProtocol.TBinaryProtocol.Factory()

    # Use TNonblockingServer for non-blocking behavior
    server = TServer.TNonblockingServer(processor, tfactory, transport, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')

    server.serve()
