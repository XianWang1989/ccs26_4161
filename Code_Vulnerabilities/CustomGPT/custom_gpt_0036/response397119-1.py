
class Hi(object):
    def __init__(self):
        self.answer = 'hi'

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)

class Goodbye(object):
    def __init__(self):
        self.hi_instance = Hi()  # Create a single instance of Hi

    def bye(self):
        self.hi_instance.change()  # Use the shared instance 

# Create a Goodbye instance        
goodbye_instance = Goodbye()
goodbye_instance.bye()           # This will print 'bye'

# Access the same Hi instance to print the updated answer
goodbye_instance.hi_instance.printer()  # This will print 'bye'
