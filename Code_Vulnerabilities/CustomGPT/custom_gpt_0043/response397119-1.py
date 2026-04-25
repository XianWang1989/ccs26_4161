
class Hi(object):
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

# Run the code
goodbye_instance = Goodbye()
goodbye_instance.bye()  # This will change the answer to 'bye'
Hi.printer()  # This will now print 'bye'
