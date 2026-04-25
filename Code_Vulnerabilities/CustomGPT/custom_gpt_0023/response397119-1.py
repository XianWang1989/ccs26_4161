
class Hi:
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

# Create a single instance of Hi
hi_instance = Hi()

class Goodbye:
    def bye(self):
        hi_instance.change()  # Use the shared instance

# Call methods using the shared instance
goodbye = Goodbye()
goodbye.bye()
hi_instance.printer()  # Use the shared instance
