
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from my_thrift_module import MyService  # Replace with your actual service module


class ServiceHandler:
    def your_service_method(self, args):
        # Your service logic here
        return "Response"


def run_server(port):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TServerSocket for transport
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use a factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()


if __name__ == '__main__':
    run_server(9090)  # Replace with your desired port
