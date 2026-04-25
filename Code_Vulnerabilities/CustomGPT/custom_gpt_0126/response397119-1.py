
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


# Create an instance of Hi
hi_instance = Hi()

# Create an instance of Goodbye and pass the hi_instance
goodbye_instance = Goodbye(hi_instance)

# Call the methods
goodbye_instance.bye()  # This will print 'bye'
hi_instance.printer()   # This will print 'bye'
