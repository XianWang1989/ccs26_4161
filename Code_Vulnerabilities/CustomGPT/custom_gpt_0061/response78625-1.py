
from thrift import Thrift
from thrift.server import TServer
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from your_service import MyService  # Replace with your actual service module
from your_handler import ServiceHandler  # Replace with your actual handler

def main():
    # Set handler to our implementation
    handler = ServiceHandler()

    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)

    # Use TTransport.TFramedTransport as the transport factory
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Set server with the correct transport factory
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')
    server.serve()

if __name__ == '__main__':
    port = 9090  # Set your desired port here
    main()
