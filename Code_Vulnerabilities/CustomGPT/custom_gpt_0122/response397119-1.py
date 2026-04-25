
class Hi(object):
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

# Create a single instance of Hi
hi_instance = Hi()

class Goodbye(object):
    def bye(self):
        hi_instance.change()

# Use the shared instance
goodbye = Goodbye()
goodbye.bye()  # Outputs: 'bye'
hi_instance.printer()  # Outputs: 'bye'
