
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Implement your service handler
class ServiceHandler:
    def your_method(self):
        # Implementation of your method
        pass

def main():
    port = 9090  # Specify your server port

    # Set handler to your implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create server socket and transport factory
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use Factory here
    pfactory = TBinaryProtocol.TBinaryProtocol.Factory()

    # Set up the threaded server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    main()
