
class Hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Update class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)  # Access the class variable

class Goodbye(object):
    def bye(self):
        Hi().change() 

# Test the code
goodbye = Goodbye()
goodbye.bye()  # Outputs: 'bye'
Hi().printer()  # Outputs: 'bye'
