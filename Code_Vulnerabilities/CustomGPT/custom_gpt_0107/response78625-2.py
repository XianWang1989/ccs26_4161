
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

# Assuming MyService is defined elsewhere

def run_client():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TFramedTransport(transport)  # Use the same transport
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = MyService.Client(protocol)

    # Open the transport
    transport.open()

    # Make your service calls here
    # Example: result = client.your_method()

    transport.close()

if __name__ == "__main__":
    run_client()
