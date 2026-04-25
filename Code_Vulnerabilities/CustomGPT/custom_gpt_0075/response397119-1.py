
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

# Pass the same instance to Goodbye
goodbye = Goodbye(hi_instance)
goodbye.bye()   # Outputs: 'bye'
hi_instance.printer()  # Outputs: 'bye'
