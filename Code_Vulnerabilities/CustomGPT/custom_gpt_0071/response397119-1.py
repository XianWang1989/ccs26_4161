
class Hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Change the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)  # Print the class variable

class Goodbye(object):
    def bye(self):
        Hi().change() 

goodbye = Goodbye()
goodbye.bye()

hi_instance = Hi()
hi_instance.printer()
