
class Hi:
    # Class variable to maintain state
    answer = 'hi'

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye:
    def bye(self):
        Hi.change() 

Goodbye().bye()    # Output: 'bye'
Hi.printer()       # Output: 'bye'
