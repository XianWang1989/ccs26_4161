
from thrift import Thrift
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Import your generated service classes (replace MyService with your actual service)
# from your_service import MyService

class ServiceHandler:
    # Implement your service methods here
    pass

if __name__ == '__main__':
    port = 9090  # Define your port

    # Create the handler to implement your service
    handler = ServiceHandler()

    processor = MyService.Processor(handler)  # Replace MyService with your actual service
    transport = TSocket.TServerSocket(port=port)

    # Use TFramedTransport to allow for a non-blocking server
    tfactory = TTransport.TFramedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # Create the server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('Python Server has started listening on port ' + str(port))
    print('################################################')

    # Start the server
    server.serve()
