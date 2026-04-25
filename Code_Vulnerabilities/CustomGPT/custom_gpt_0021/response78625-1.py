
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
from my_thrift_service import MyService  # Import your generated service files

class ServiceHandler(MyService.Iface):
    # Implement your service methods here
    def my_method(self, input):
        return "Response from my_method with input: " + input

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)

    tfactory = TTransport.TFramedTransportFactory()  # Use Framed Transport Factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print("Python Non-blocking Thrift Server has started listening on port 9090")
    print("################################################")
    server.serve()

if __name__ == "__main__":
    main()
