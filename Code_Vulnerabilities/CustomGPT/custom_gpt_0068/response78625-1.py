
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_module import MyService  # Import your generated Thrift service

class ServiceHandler:
    # Your implementation of the service methods
    def your_method(self):
        # Implement your service logic here
        pass

def run_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket for the transport
    transport = TSocket.TServerSocket(port=port)

    # Use TFramedTransport for non-blocking IO
    tfactory = TTransport.TFramedTransport.Factory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set the server to the TThreadedServer or TSimpleServer based on your needs
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server(9090)  # Replace 9090 with your desired port number
