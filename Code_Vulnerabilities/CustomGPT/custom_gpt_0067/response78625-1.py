
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from your_thrift_module import MyService  # Adjust import for your service

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket and proper transport
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()  # Use Factory here
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')

    server.serve()

if __name__ == '__main__':
    main()
