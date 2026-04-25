
class Hi(object):
    answer = 'hi'  # Class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye(object):
    def bye(self):
        Hi.change()  

# Example usage
goodbye = Goodbye()
goodbye.bye()        # Outputs: 'bye'
Hi.printer()         # Outputs: 'bye'
