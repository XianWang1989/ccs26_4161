
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_service import MyService  # Replace with your actual Thrift service implementation

class ServiceHandler:
    # Implement your service methods here
    def your_method(self):
        pass

def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Set up a server socket
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use the Factory class
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server(9090)  # Change the port as necessary
