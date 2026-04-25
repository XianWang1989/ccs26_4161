
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated Thrift code
from your_thrift_module import MyService

class ServiceHandler:
    # Implement your service methods here

if __name__ == "__main__":
    port = 9090  # Set your desired port

    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TFramedTransport as input and output transport factories
    tfactory = TTransport.TFramedTransport.Factory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up the server with corrected transport and protocol factories
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
