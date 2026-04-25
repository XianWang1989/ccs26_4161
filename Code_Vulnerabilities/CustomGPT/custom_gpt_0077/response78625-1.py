
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_file import MyService  # Import your generated Thrift service

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket for incoming connections
    transport = TSocket.TServerSocket(port=9090)

    # Use TTransport to wrap the socket
    tfactory = TTransport.TFramedTransport.Factory()  
    pfactory = TBinaryProtocol.TBinaryProtocol.Factory()

    # Set up the server with the proper factory classes
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
