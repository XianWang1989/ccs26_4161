
class Hi(object):
    # Class variable
    answer = 'hi'

    def change(self):
        Hi.answer = 'bye'  # Modify the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change() 

Goodbye().bye()
Hi().printer()
