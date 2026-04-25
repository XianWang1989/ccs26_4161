
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from my_service import MyService  # Import your service definition

class ServiceHandler:
    def my_method(self):
        return "Hello from the non-blocking server!"

if __name__ == '__main__':
    port = 9090

    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use the TServerSocket class
    transport = TSocket.TServerSocket(port=port)

    # Use TTransport.TBufferedTransport for better performance
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create a threaded server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
