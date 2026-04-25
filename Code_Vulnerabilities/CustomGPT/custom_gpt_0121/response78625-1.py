
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_service import MyService  # Change to your actual service

class ServiceHandler(MyService.Iface):
    # Implement your service methods here
    def your_method(self, args):
        # Your logic
        return result

if __name__ == '__main__':
    port = 9090  # Set your desired port here
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Use the factory instead of the instance
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server to ThreadPool for non-blocking behavior
    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()
