
class Hi(object):
    answer = 'hi'  # Class-level variable

    def change(self):
        Hi.answer = 'bye'  # Modify the class-level variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)  # Access the class-level variable

class Goodbye(object):
    def bye(self):
        Hi().change()

# Example usage
goodbye = Goodbye()
goodbye.bye()  # Outputs: 'bye'
Hi().printer()  # Outputs: 'bye'
