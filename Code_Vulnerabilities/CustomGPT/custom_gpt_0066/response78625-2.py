
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from MyService import MyService

# Create transport and protocol
transport = TSocket.TSocket('localhost', port)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# Open transport
transport = tfactory.getTransport(transport)
protocol = pfactory.getProtocol(transport)

client = MyService.Client(protocol)

try:
    transport.open()
    # Use client methods here
finally:
    transport.close()
