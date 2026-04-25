
class hi:
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class goodbye:
    def __init__(self, hi_instance):
        self.hi_instance = hi_instance

    def bye(self):
        self.hi_instance.change()

# Create a single instance of hi
hi_instance = hi()

# Use this instance in goodbye
goodbye_instance = goodbye(hi_instance)
goodbye_instance.bye()

# Print the answer from the same instance
hi_instance.printer()
