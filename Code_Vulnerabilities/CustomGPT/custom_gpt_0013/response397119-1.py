
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

# Create instances and call methods
goodbye = Goodbye()
goodbye.bye()        # Outputs: bye
hi_instance = Hi()
hi_instance.printer()  # Outputs: bye
