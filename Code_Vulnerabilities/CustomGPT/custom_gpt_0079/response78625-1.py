
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Your service implementation
class ServiceHandler:
    def your_method(self):
        # Implementation here
        pass

def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create server socket
    transport = TSocket.TServerSocket(port=port)

    # Use the correct transport factory
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print 'Python Server has started listening on port ' + str(port)
    print '################################################'
    server.serve()

if __name__ == "__main__":
    run_server(port=9090)
