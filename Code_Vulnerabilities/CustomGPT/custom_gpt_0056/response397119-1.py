
class Hi(object):
    answer = 'hi'  # Class variable

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

# Create an instance of Goodbye and call the bye method
goodbye = Goodbye()
goodbye.bye()

# Print the answer using Hi's printer method
Hi.printer()
