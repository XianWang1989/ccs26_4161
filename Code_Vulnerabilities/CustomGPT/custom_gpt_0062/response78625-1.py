
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your service definitions here
# from your_service import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create transport and protocol factories
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server configuration
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    try:
        server.serve()
    except Thrift.TTransport.TTransportException as e:
        print("Transport error: ", e)
    except Exception as e:
        print("Server error: ", e)

if __name__ == '__main__':
    run_server(9090)  # Use your desired port
