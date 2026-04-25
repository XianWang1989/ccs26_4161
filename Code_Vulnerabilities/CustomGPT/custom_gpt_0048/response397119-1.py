
class Hi(object):
    answer = 'hi'  # Class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'  # Change class variable
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye(object):
    def bye(self):
        Hi.change()  # Call change method on Hi class

Goodbye().bye()  # Changes answer to 'bye'
Hi.printer()     # Prints 'bye'
