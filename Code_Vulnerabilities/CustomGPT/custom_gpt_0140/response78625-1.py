
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from your_thrift_module import MyService  # Adjust this import to your generated Thrift code

class ServiceHandler:
    def your_method(self, ...):
        # Implementation of your service method
        pass

def main():
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()  # Use FramedTransportFactory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port 9090')
    server.serve()

if __name__ == '__main__':
    main()
