
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from myservice import MyService  # Import your generated service class

class ServiceHandler:
    def my_function(self):
        return "Hello, Thrift!"

if __name__ == '__main__':
    # Set handler to your implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Using non-blocking transport
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()  # Ensure you are using TFramedTransportFactory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')
    server.serve()
