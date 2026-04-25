
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_module import MyService  # Adjust import as necessary

class ServiceHandler:
    # Implement your service methods here
    pass

def run_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket as the transport
    transport = TSocket.TServerSocket(port=port)
    # Use TFramedTransport to allow non-blocking connections
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server to threaded version
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    run_server(9090)  # Change port as needed
