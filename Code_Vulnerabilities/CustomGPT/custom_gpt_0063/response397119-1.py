
class Hi(object):
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye(object):
    def __init__(self, hi_instance):
        self.hi_instance = hi_instance

    def bye(self):
        self.hi_instance.change()

# Create a single instance of the Hi class
hi_instance = Hi()

# Pass the `hi_instance` to the Goodbye class
goodbye = Goodbye(hi_instance)
goodbye.bye()   # Output: 'bye'

# Now call printer on the same instance
hi_instance.printer()  # Output: 'bye'
