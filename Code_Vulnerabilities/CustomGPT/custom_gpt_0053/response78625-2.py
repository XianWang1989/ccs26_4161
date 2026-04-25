
from thrift.server import TNonblockingServer

if __name__ == "__main__":
    port = 9090

    handler = ServiceHandler()
    processor = MyService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransport.Factory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TNonblockingServer.TNonblockingServer(processor, transport, tfactory, pfactory)

    print('Non-blocking Python Server has started listening on port ' + str(port))
    server.serve()
