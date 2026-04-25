
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Adjust your import according to your service

class ServiceHandler:
    # Implement your service methods here
    pass

def run_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create a server socket
    transport = TSocket.TServerSocket(port=port)

    # Instead of TFramedTransport, use TTransport.TBufferedTransport
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print(f'Python Server has started listening on port {port}')
    print('################################################')

    # Start the server
    server.serve()

if __name__ == '__main__':
    run_server(9090)  # Replace 9090 with your desired port
