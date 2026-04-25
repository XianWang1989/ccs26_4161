
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated Thrift code (replace 'YourService' with the actual service name)
# from your_generated_module import MyService

class ServiceHandler:
    # Your implementation of the service methods
    def your_method(self, your_parameters):
        pass

if __name__ == '__main__':
    port = 9090  # Set your desired port

    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Non-blocking server setup
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()  # Use TBufferedTransport for simplicity
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print 'Python Server has started listening on port ' + str(port)
    print '################################################'
    server.serve()
