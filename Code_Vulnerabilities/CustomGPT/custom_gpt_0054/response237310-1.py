
import ast

class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Using ast.Expression to build a valid expression with comments
        return f'Sum({self.a}, {self.b}) # sum={self.sum}' if self.sum != self.a + self.b else f'Sum({self.a}, {self.b})'

    def __str__(self):
        # Here we ensure it only presents what Python can execute
        return repr(self)

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Outputs: 'Sum(2, 2) # sum=3'
