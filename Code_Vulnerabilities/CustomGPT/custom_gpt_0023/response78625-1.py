
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TAsyncServer
from your_service import MyService  # Import your generated thrift service

class ServiceHandler:
    def some_method(self, param):
        # Your method implementation
        return "Response from some_method"

async def start_server(port):
    handler = ServiceHandler()
    processor = MyService.Processor(handler)

    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TFramedTransportFactory()  # Change here
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TAsyncServer.TAsyncioServer(processor, transport, tfactory, pfactory)

    print('Python Async Thrift Server has started listening on port ' + str(port))
    await server.serve()

if __name__ == '__main__':
    import asyncio

    port = 9090  # Set your desired port
    asyncio.run(start_server(port))
