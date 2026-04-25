
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

# Create an instance of Hi only once
hi_instance = Hi()

# Pass the same instance to Goodbye
goodbye = Goodbye(hi_instance)
goodbye.bye()  # This will print 'bye'
hi_instance.printer()  # This will also print 'bye'
