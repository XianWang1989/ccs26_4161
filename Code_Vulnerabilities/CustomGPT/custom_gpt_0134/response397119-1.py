
class Hi:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Hi, cls).__new__(cls)
            cls._instance.answer = 'hi'
        return cls._instance

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye:
    def bye(self):
        Hi().change()  # Change the singleton instance

goodbye = Goodbye()
goodbye.bye()  # This will print 'bye'
Hi().printer()  # This will now also print 'bye' since it's the same instance
