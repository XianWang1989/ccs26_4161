
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import the generated Thrift classes
from your_thrift_module import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create a server socket
    transport = TSocket.TServerSocket(port=port)

    # Use a framed transport
    tfactory = TTransport.TTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server(port=9090)  # You can specify your desired port here
