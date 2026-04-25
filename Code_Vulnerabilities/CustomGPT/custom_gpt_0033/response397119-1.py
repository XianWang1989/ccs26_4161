
class Hi(object):
    answer = 'hi'  # Class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'  # Change the class variable
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye(object):
    def bye(self):
        Hi.change()  # Call method from Hi class

# Create instances and call methods
goodbye_instance = Goodbye()
goodbye_instance.bye()  # Outputs 'bye'
Hi.printer()  # Outputs 'bye'
