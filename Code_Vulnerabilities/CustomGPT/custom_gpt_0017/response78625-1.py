
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from your_module import MyService  # Ensure to replace with your actual service definition

class ServiceHandler:
    # Implement your service methods here
    def your_method(self):
        pass

def main():
    port = 9090  # Replace with your desired port number
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use Factory, not instance
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print(f'Python Server has started listening on port {port}')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
