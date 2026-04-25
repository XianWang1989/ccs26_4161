
class Hi(object):
    # Class variable to hold the state
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
        Hi.change()  # Change the answer to 'bye'


# Create an instance of Goodbye and call the bye method
goodbye_instance = Goodbye()
goodbye_instance.bye()

# Call the printer method from the Hi class
Hi.printer()  # This will now print 'bye'
