
class Hi(object):
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

# Create a single instance of the Hi class
hi_instance = Hi()

class Goodbye(object):
    def bye(self):
        # Use the existing hi_instance
        hi_instance.change()

# Call the methods
goodbye = Goodbye()
goodbye.bye()  # Outputs 'bye'
hi_instance.printer()  # Outputs 'bye'
