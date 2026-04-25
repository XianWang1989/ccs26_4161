
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from your_service import MyService  # Replace with your service import

class ServiceHandler:
    # Implement your service methods here
    pass

if __name__ == '__main__':
    port = 9090  # Choose your port

    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TTransport.TFramedTransport as a factory
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Use TThreadedServer for non-blocking
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
