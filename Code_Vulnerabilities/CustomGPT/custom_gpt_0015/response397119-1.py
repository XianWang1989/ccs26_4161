
class Hi:
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Modify the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye:
    def bye(self):
        Hi().change()  # Change the class variable

# Create instances and call methods
goodbye = Goodbye()
goodbye.bye()        # Outputs 'bye'
hi_instance = Hi()
hi_instance.printer()  # Outputs 'bye'
