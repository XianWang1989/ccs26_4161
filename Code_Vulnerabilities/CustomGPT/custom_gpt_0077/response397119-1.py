
class Hi:
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye:
    def __init__(self):
        self.hi_instance = Hi()  # Keep a single instance of Hi

    def bye(self):
        self.hi_instance.change()  # Use the existing instance

# Create the Goodbye instance
goodbye_instance = Goodbye()
goodbye_instance.bye()  # Outputs 'bye'

# Use the same instance to print the answer
goodbye_instance.hi_instance.printer()  # Outputs 'bye'
