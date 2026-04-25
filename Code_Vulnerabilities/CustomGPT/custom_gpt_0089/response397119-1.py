
class Hi(object):
    answer = 'hi'  # Class attribute

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye(object):
    def bye(self):
        Hi.change()  # Call the change method

# Create an instance of Goodbye and call the bye method
Goodbye().bye()
# Call the printer method from the Hi class
Hi.printer()
