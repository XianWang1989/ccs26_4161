
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from your_thrift_module import MyService  # Adjust according to your generated module

def main():
    port = 9090  # Example port number
    transport = TSocket.TSocket('localhost', port)
    tfactory = TTransport.TFramedTransport.Factory()  # Use the same transport factory as the server
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Creating the client
    client = MyService.Client(protocol)

    # Connect to the server
    transport.open()

    # Call your method
    response = client.your_method("Your request data")
    print(response)

    # Close the connection
    transport.close()

if __name__ == '__main__':
    main()
