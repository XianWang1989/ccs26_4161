
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer
from my_service import MyService  # Replace with your actual service definition

class ServiceHandler:
    def my_function(self):
        # Implement your service logic here
        return "Response from my_function"

def main():
    port = 9090  # Set your desired port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Use TNonblockingServer for non-blocking behavior
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    server.serve()

if __name__ == "__main__":
    main()
