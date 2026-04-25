
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


hi_instance = Hi()  # Create one instance of Hi
goodbye = Goodbye(hi_instance)  # Pass the instance to Goodbye

goodbye.bye()  # This will change the answer to 'bye'
hi_instance.printer()  # This will now also print 'bye'
