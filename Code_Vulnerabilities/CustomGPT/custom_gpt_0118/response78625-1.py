
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated Thrift code
from your_service import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Example port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create a server socket
    transport = TSocket.TServerSocket(port=port)

    # Use framed transport for non-blocking
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    try:
        server.serve()
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
