
class hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        hi.answer = 'bye'  # Modify the class variable
        print(hi.answer)

    def printer(self):
        print(hi.answer)

class goodbye(object):
    def bye(self):
        hi().change()  # Change the class variable through an instance

goodbye().bye()
hi().printer()  # Print the updated class variable
