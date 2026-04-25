
if __name__ == "__main__":
    factory = WebSocketClientFactory("ws://localhost:7096")
    job_queue = Queue()
    factory.protocol = lambda: BridgeSocket(job_queue)  # Use a lambda to create instances

    connectWS(factory)
    reactor.run()
