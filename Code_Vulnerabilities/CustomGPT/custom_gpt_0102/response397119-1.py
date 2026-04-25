
class Hi:
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'  # Modify the class variable
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye:
    def bye(self):
        h = Hi()  # Create instance of Hi
        h.change() 

# Create instances and call methods
g = Goodbye()
g.bye()

h2 = Hi()
h2.printer()  # Now this will print 'bye'
