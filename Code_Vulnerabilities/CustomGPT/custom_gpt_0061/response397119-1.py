
class Hi(object):
    # Class variable to store the answer
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

# Now print the answer using the class method
Hi.printer()
