
from thrift import Thrift
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_module import MyService  # Replace with your actual generated Thrift module

class ServiceHandler:
    # Implement your service methods here
    def your_method_name(self, param):
        return "Response from method"

def main():
    port = 9090  # Replace with your desired port
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()  # Change to TBufferedTransportFactory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up server
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)  # Use TSimpleServer for easier setup

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
