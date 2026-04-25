
class Hi(object):
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye(object):
    # Using a class-level variable to store the instance
    hi_instance = Hi()

    def bye(self):
        self.hi_instance.change()

# Create an instance of Goodbye and call its bye method
goodbye_instance = Goodbye()
goodbye_instance.bye()

# Call the printer method on the same instance of Hi
goodbye_instance.hi_instance.printer()
