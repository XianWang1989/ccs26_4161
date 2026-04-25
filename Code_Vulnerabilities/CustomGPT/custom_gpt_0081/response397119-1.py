
class Hi(object):
    answer = 'hi'  # Class variable

    @classmethod
    def change(cls):
        cls.answer = 'bye'  # Modify the class variable
        print(cls.answer)

    @classmethod
    def printer(cls):
        print(cls.answer)

class Goodbye(object):

    def bye(self):
        Hi.change() 

# Create a Goodbye instance and call bye method
Goodbye().bye()
# Create a Hi instance and call printer method
Hi.printer()  # This will now print 'bye'
