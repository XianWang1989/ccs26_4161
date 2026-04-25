
class hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        hi.answer = 'bye'  # Update the class variable
        print(hi.answer)

    def printer(self):
        print(hi.answer)

class goodbye(object):
    def bye(self):
        hi().change() 

# Create instances and call methods
goodbye().bye()  # This will print 'bye'
hi().printer()   # This will also print 'bye'
