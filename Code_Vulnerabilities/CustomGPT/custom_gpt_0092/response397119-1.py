
class Hi:
    answer = 'hi'  # Class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye:
    def bye(self):
        Hi.change()

# Example usage
goodbye_instance = Goodbye()
goodbye_instance.bye()  # Output: 'bye'
Hi.printer()  # Output: 'bye'
