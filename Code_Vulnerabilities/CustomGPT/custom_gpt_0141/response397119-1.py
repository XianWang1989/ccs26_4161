
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
        # Use the existing instance instead of creating a new one
        hi_instance.change()

# Create an instance of Goodbye and call the bye method
goodbye = Goodbye()
goodbye.bye()

# Print the answer using the same Hi instance
hi_instance.printer()
