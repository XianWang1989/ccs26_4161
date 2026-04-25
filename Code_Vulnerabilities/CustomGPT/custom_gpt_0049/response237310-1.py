
import ast

class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent = self.sum == self.a + self.b
        # Construct a string using an AST node, allowing us to add comments
        if consistent:
            return 'Sum({}, {})'.format(self.a, self.b)
        else:
            # We create a string that Python can parse, and we add a comment
            return 'Sum({}, {})  # sum={}'.format(self.a, self.b, self.sum)

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update() 
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
