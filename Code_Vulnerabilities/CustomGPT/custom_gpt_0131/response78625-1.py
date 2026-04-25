
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated Thrift classes
from your_thrift_module import MyService

class ServiceHandler:
    # Define your service methods here
    pass

def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Setting up the transport
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use the factory instead of TFramedTransport itself
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server(9090)
