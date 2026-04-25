
class Hi(object):
    answer = 'hi'  # Class variable shared among all instances

    def change(self):
        Hi.answer = 'bye'  # Change the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change()  # Calls change on an instance of Hi

Goodbye().bye()  # Outputs 'bye'
Hi().printer()   # Outputs 'bye'
