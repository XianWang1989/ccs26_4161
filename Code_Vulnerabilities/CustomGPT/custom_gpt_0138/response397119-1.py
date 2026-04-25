
class Hi(object):
    answer = 'hi'  # Class attribute

    def change(self):
        Hi.answer = 'bye'  # Change class attribute
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change() 

Goodbye().bye()
Hi().printer()
