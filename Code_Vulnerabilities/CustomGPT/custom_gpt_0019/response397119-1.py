
class Hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Change the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change()

# Create instances and call methods
goodbye = Goodbye()
goodbye.bye()  # Outputs 'bye'

hi_instance = Hi()
hi_instance.printer()  # Outputs 'bye'
