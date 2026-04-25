
from thrift import Thrift
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from your_thrift_module import MyService  # Adjust this import as per your service definition

class ServiceHandler:
    # Implement your service methods here
    def your_method(self, args):
        # Handle your request
        return "Response Data"

def main():
    port = 9090  # Example port number
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use .Factory() to create the factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
