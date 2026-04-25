
class Hi(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Hi, cls).__new__(cls)
            cls._instance.answer = 'hi'
        return cls._instance

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye(object):
    def bye(self):
        hi_instance = Hi()
        hi_instance.change()

# Run the code
goodbye_instance = Goodbye()
goodbye_instance.bye()  # This will change the answer to 'bye'

hi_instance = Hi()  # Get the same instance
hi_instance.printer()  # This will now print 'bye'
