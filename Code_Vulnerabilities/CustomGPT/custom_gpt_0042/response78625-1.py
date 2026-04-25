
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from my_service import MyService  # Make sure to import your generated Thrift service

class ServiceHandler:
    # Implement your service methods here
    pass

def main():
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Create server transport
    transport = TSocket.TServerSocket(port=9090)

    # Use FramedTransport for non-blocking
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    server.serve()

if __name__ == "__main__":
    main()
