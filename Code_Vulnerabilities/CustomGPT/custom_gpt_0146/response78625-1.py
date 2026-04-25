
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_generated_code import MyService  # Import your generated Thrift service

class ServiceHandler:
    # Your implementation here
    pass

if __name__ == '__main__':
    port = 9090  # Specify your port

    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TFramedTransportFactory instead of TFramedTransport
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
