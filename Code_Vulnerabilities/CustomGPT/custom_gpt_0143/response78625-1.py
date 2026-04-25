
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from thrift.server import TNonblockingServer
from your_thrift_file import MyService  # Import your service definition

class ServiceHandler:
    # Implement your service methods here
    def your_method(self):
       pass

def main():
    port = 9090  # Specify your port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Setup transport
    server_transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use framed transport factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TNonblockingServer.TNonblockingServer(processor, server_transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
