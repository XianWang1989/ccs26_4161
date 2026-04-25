
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer

# Dummy service handler
class ServiceHandler:
    def ping(self):
        return "pong"

# Your Thrift service
from your_thrift_gen import MyService  # Ensure to adjust the import according to your generated Thrift code

def main():
    port = 9090  # Set your desired port

    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use Factory, not instance
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server
    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    main()
