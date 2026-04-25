
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

# Creating a single instance of Hi and passing it to Goodbye
hi_instance = Hi()
goodbye_instance = Goodbye(hi_instance)

# Calling the methods
goodbye_instance.bye()  # This will change the answer to 'bye'
hi_instance.printer()   # This will now print 'bye'
