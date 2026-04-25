
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

# Create a single instance of Hi
hi_instance = Hi()

# Create an instance of Goodbye and pass the hi_instance
goodbye = Goodbye(hi_instance)
goodbye.bye()  # This will print 'bye'

# Now use the same hi_instance to print
hi_instance.printer()  # This will also print 'bye'
