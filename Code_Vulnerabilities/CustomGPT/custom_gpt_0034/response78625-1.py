
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from my_service import MyService  # Import your service definition

class ServiceHandler:
    # Implement your service methods here
    pass

def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TTransport.TFramedTransport as the transport factory
    tfactory = TTransport.TFramedTransportFactory()
    # Use the binary protocol
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

# Example usage
if __name__ == "__main__":
    run_server(9090)  # Specify your desired port
