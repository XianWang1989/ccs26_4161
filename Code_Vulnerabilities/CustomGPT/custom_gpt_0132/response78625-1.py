
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Replace with your actual service module

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Set your desired port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TFramedTransport and TBinaryProtocol
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print(f'Python Server has started listening on port {port}')
    print('################################################')
    server.serve()

if __name__ == "__main__":
    main()
