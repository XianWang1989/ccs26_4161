
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service_module import MyService  # Import your service here
from your_handler_module import ServiceHandler  # Import your handler here

def main():
    # Set handler to your implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Correctly create transport factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    port = 9090  # Change to your desired port
    main()
