
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from your_service import MyService  # Replace with your actual service module

class ServiceHandler:
    # Implement required methods for your service here
    pass

def run_thrift_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()  # Use TBufferedTransportFactory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    run_thrift_server(9090)  # Replace with your desired port
