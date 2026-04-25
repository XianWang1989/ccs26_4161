
class hi(object):
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class goodbye(object):
    def __init__(self, hi_instance):
        self.hi_instance = hi_instance

    def bye(self):
        self.hi_instance.change() 

# Create a single instance of the `hi` class
hi_instance = hi()

# Use this instance in `goodbye`
goodbye_instance = goodbye(hi_instance)

# Call methods
goodbye_instance.bye()  # This will change the answer to 'bye'
hi_instance.printer()   # This will now print 'bye'
