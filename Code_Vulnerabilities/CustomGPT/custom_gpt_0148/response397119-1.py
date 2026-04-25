
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

# Create an instance of Goodbye and call bye
Goodbye().bye()
# Call printer method to see the updated value
Hi.printer()
