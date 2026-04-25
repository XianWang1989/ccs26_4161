
class Hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Modify the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change()  # Calls change method

# Create instances and call methods
goodbye = Goodbye()
goodbye.bye()

hi_instance = Hi()
hi_instance.printer()  # Now this will print 'bye'
