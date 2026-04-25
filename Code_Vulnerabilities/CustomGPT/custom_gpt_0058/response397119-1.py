
class hi(object):
    answer = 'hi'  # Make this a class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class goodbye(object):
    def bye(self):
        hi.change() 

goodbye().bye()      # Output: 'bye'
hi.printer()         # Output: 'bye'
