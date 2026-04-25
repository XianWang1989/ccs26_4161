
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from your_service import MyService  # Adjust import according to your service's generated files

class ServiceHandler:  
    # Implement your service methods here
    pass

def run_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransport.Factory()  # Change to BufferedTransport
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == "__main__":
    run_server(9090)  # Replace 9090 with your desired port
