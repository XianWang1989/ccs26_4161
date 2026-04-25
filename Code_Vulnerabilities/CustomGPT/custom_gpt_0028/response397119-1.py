
class hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        hi.answer = 'bye'  # Modify the class variable
        print(hi.answer)

    def printer(self):
        print(hi.answer)

class goodbye(object):
    def bye(self):
        hi().change() 

# Running the code
goodbye().bye()  # Output: bye
hi().printer()   # Output: bye
