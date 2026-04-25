
class Hi(object):
    # Class variable shared among all instances
    answer = 'hi'

    def change(self):
        Hi.answer = 'bye'  # Change the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change()  # Calls change method

# Test the code
goodbye = Goodbye()
goodbye.bye()  # Outputs 'bye'
hi_instance = Hi()
hi_instance.printer()  # Outputs 'bye'
