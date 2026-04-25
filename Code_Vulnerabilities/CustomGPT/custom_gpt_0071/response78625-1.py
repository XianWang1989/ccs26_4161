
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Replace with your actual service

class ServiceHandler:
    # Define your service methods here
    pass

def run_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use the factory here
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server(9090)  # Replace with your desired port
