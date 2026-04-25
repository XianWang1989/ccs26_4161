
class hi(object):
    answer = 'hi'  # Class variable shared by all instances

    def change(self):
        hi.answer = 'bye'  # Changing the class variable
        print(self.answer)

    def printer(self):
        print(hi.answer)  # Accessing the class variable

class goodbye(object):
    def bye(self):
        hi().change() 

goodbye().bye()  # This will print 'bye'
hi().printer()  # This will also print 'bye'
