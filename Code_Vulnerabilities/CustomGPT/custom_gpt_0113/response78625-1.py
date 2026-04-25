
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_file import MyService  # Adjust this import based on your service definition

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Set your port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use .Factory() for factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Use TThreadPoolServer for non-blocking
    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
