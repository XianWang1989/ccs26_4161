
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from your_thrift_module import MyService  # Adjust this import as necessary

def main():
    transport = TSocket.TSocket('localhost', 9090)
    tfactory = TTransport.TFramedTransportFactory()
    protocol = TBinaryProtocol.TBinaryProtocolFactory()

    # Create a transport and protocol
    transport = tfactory.getTransport(transport)
    protocol = protocol.getProtocol(transport)

    # Open the transport
    transport.open()

    client = MyService.Client(protocol)
    # Call your methods
    # client.your_method()

    # Close the transport
    transport.close()

if __name__ == '__main__':
    main()
