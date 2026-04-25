
def onMessage(self, payload, isBinary):
    self.producer_queue.put(payload)
