
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated service code here
# from your_service import MyService

class ServiceHandler:
    def example_method(self):
        return "Hello, world!"

def main():
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create server socket
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransport.Factory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server with non-blocking configuration
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')

    try:
        server.serve()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
