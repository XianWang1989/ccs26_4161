
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from my_service import MyService  # Import your generated service code

class ServiceHandler:
    def my_method(self):
        return "Hello from the Thrift server!"

def run_server(port=9090):
    # Set handler to our implementation
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    # Set up transport and protocol
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Changed to Factory
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set up server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    run_server()
