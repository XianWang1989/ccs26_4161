
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Assume MyService and ServiceHandler are defined elsewhere
class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    port = 9090  # Change to your desired port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket to create a socket
    transport = TSocket.TServerSocket(port=port)
    # Use TBufferedTransport as input/output transport
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
