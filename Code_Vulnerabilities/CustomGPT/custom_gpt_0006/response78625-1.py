
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from my_service import MyService  # Ensure this imports your Thrift service

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Set your desired port
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TTransport.TFramedTransport for both input and output
    tfactory = TTransport.TFramedTransport.Factory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create server with correct transport and protocol factories
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
