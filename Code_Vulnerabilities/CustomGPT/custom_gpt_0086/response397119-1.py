
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

# Use that instance in the Goodbye class
goodbye_instance = Goodbye(hi_instance)

# Call methods
goodbye_instance.bye()  # Outputs: bye
hi_instance.printer()   # Outputs: bye
