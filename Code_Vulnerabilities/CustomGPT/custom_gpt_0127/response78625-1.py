
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
from your_service import MyService  # Adjust the import based on your service file

class ServiceHandler(MyService.Iface):
    def your_method(self, arg):
        # Your implementation here
        return "Response"

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Use TNonblockingServer for non-blocking behavior
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()  # Use Factory here
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
