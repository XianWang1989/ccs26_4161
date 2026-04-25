
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
        hi_instance.change()  # Use the existing instance

# Create an instance of Goodbye and call bye
goodbye = Goodbye()
goodbye.bye ()

# Call printer on the existing Hi instance
hi_instance.printer()
