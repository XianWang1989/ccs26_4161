
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Using a comment-like structure that Python will ignore
        return f'Sum({self.a}, {self.b}) # sum={self.sum}'

    def __repr__(self):
        # Python will parse this; the comment-like part is ignored
        return f'Sum({self.a}, {self.b}); # sum={self.sum}' if self.sum != self.a + self.b else f'Sum({self.a}, {self.b})'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2) # sum=3'

# As a parsed expression
code_repr = repr(x)
print(code_repr)  # Output: 'Sum(2, 2); # sum=3'
