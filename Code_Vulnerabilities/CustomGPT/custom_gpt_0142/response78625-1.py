
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from my_service import MyService  # Replace with your actual service

class ServiceHandler:
    # Implement the methods defined in your Thrift service here
    def your_method(self, some_param):
        # Your implementation
        return "Response from your_method"

def main():
    port = 9090  # Set your port number
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use the factory properly
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Use TNonblockingServer for a non-blocking server
    server = TServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    try:
        server.serve()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
