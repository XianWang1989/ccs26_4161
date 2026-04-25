
class Hi(object):
    # Class variable
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

# Create an instance of Goodbye and call bye
Goodbye().bye()

# Create an instance of Hi and call printer
Hi.printer()
