
class hi(object):
    answer = 'hi'  # Class variable

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

goodbye().bye()
hi.printer()  # This will now print 'bye'
