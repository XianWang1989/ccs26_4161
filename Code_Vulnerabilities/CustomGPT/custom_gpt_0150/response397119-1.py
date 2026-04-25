
class Hi(object):
    # Class variable to hold the answer
    answer = 'hi'

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye(object):
    def bye(self):
        Hi.change()

# Create instances and call methods
goodbye = Goodbye()
goodbye.bye()      # Output: 'bye'
Hi.printer()       # Output: 'bye'
