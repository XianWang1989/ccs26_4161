
class hi(object):
    # Class variable shared by all instances
    answer = 'hi'

    def change(self):
        hi.answer = 'bye'  # Change the class variable
        print(hi.answer)

    def printer(self):
        print(hi.answer)  # Print the class variable

class goodbye(object):
    def bye(self):
        hi().change() 

# Creating an instance of goodbye and calling bye
goodbye().bye()

# Creating an instance of hi and calling printer
hi().printer()
