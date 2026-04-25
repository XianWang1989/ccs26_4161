
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
        Hi().change()

# Create an instance of Goodbye and call its method
goodbye = Goodbye()
goodbye.bye()

# Now, get the shared instance of Hi to print the answer
hi_instance = Hi()
hi_instance.printer()
