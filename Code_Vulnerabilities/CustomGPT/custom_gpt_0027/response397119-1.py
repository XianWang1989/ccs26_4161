
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

# Create a single instance of hi
hi_instance = hi()

# Pass the instance to goodbye
goodbye_instance = goodbye(hi_instance)
goodbye_instance.bye()

# Print the answer using the same hi instance
hi_instance.printer()
