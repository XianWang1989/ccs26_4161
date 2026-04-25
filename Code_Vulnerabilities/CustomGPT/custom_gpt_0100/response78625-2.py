
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

# Configure client
transport = TSocket.TSocket('localhost', port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

transport = tfactory.getTransport(transport)
protocol = pfactory.getProtocol(transport)

client = MyService.Client(protocol)

try:
    transport.open()
    # Call your service methods here
finally:
    transport.close()
