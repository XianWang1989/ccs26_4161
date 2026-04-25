
class Hi(object):
    # Class variable shared among all instances
    answer = 'hi'

    def change(self):
        Hi.answer = 'bye'  # Change the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)  # Access the class variable

class Goodbye(object):
    def bye(self):
        Hi().change()  # Call the change method

# Driver code
goodbye = Goodbye()
goodbye.bye()  # This will change the answer to 'bye'
hi_instance = Hi()
hi_instance.printer()  # This will print 'bye'
