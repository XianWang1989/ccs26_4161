
class Hi(object):
    _instance = None  # Class variable to hold the singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Hi, cls).__new__(cls)  # Create instance
            cls._instance.answer = 'hi'  # Initialize answer
        return cls._instance

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)


class Goodbye(object):
    def bye(self):
        Hi().change()  # Modify the singleton instance


goodbye = Goodbye()
goodbye.bye()
Hi().printer()  # Access the same instance
