
class Hi:
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Change the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)  # Print the class variable

class Goodbye:
    def bye(self):
        Hi().change() 

# Test the classes
goodbye = Goodbye()
goodbye.bye()  # Output: 'bye'
Hi().printer()  # Output: 'bye'
