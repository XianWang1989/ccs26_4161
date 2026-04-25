
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_module import MyService  # Replace with your actual module name

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Specify the port you want to use
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use TFramedTransportFactory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server with correct transport factory
    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print(f'Python Server has started listening on port {port}')
    print('################################################')

    server.serve()

if __name__ == '__main__':
    main()
