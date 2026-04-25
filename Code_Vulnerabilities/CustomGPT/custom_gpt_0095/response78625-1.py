
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_file import MyService  # Import your generated Thrift code

class ServiceHandler:
    # Implement your service methods here
    pass

def run_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use the right transport factory for TThreadedServer
    tfactory = TTransport.TBufferedTransportFactory()  # Use TBufferedTransportFactory instead
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print(f'Python Server has started listening on port {port}')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server(9090)  # Change port number as needed
