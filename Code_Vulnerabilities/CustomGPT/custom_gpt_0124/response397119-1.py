
class Hi:
    answer = 'hi'  # class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye:
    def bye(self):
        Hi.change()  # change the class variable

Goodbye().bye()  # Outputs 'bye'
Hi.printer()     # Now also outputs 'bye'
