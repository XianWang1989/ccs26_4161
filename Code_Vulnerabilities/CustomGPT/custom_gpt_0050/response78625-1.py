
# Import necessary Thrift classes
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Your service handler implementation
class ServiceHandler:
    # Implement your service methods here
    def your_method(self):
        pass

# Main server code
if __name__ == '__main__':
    port = 9090  # Set your port

    # Set handler to your implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Setup the server transport and protocol
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use Factory here
    pfactory = TBinaryProtocol.TBinaryProtocol.Factory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print(f'Python Server has started listening on port {port}')
    print('################################################')
    server.serve()
