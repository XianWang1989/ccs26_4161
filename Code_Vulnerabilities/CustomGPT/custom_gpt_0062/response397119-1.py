
class Hi:
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye:
    def __init__(self, hi_instance):
        self.hi_instance = hi_instance

    def bye(self):
        self.hi_instance.change()

# Create an instance of Hi
hi_instance = Hi()

# Pass the instance to Goodbye
goodbye_instance = Goodbye(hi_instance)
goodbye_instance.bye()

# Print the updated answer
hi_instance.printer()
