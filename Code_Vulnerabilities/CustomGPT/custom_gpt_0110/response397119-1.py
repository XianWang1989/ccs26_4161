
class Hi:
    # Class variable to store the answer
    answer = 'hi'

    def change(self):
        Hi.answer = 'bye'
        print(Hi.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye:
    def bye(self):
        Hi().change()

# Create instances and call the methods
goodbye_instance = Goodbye()
goodbye_instance.bye()  # Outputs 'bye'
Hi.printer()            # Outputs 'bye'
