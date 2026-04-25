
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

# Create an instance of Goodbye, passing the Hi instance
goodbye_instance = Goodbye(hi_instance)

# Call the change method
goodbye_instance.bye()

# Call the printer method on the same hi_instance
hi_instance.printer()
