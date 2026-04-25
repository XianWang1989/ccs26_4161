
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
        Hi.change()  # Change the class variable

# Create an instance of Goodbye and call bye
Goodbye().bye()
# Now, call the printer method to see the updated value
Hi.printer()
