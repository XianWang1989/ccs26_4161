
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Format the output as an expression that Python can parse
        comment = '' if self.sum == self.a + self.b else f' # sum={self.sum}'
        return f'Sum({self.a}, {self.b}){comment}'

# Helper function to print safely
def pretty_print(obj):
    # If the object's state is inconsistent, it will include the "comment"
    print(str(obj))

# Demo:
x = Sum(1, 2)
pretty_print(x)  # Output: Sum(1, 2)

x.a = 2
pretty_print(x)  # Output: Sum(2, 2) # sum=3
