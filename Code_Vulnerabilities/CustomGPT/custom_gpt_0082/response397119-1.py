
class Hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Modify the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)  # Access the class variable

class Goodbye(object):
    def bye(self):
        Hi().change() 

Goodbye().bye()
Hi().printer()
