
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Create a string representation that Python will parse
        consistent_sum = self.a + self.b
        inconsistency_comment = '' if self.sum == consistent_sum else f' # sum={self.sum}'
        return f'Sum({self.a}, {self.b}){inconsistency_comment}'

# Demo
x = Sum(1, 2)
print(repr(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(repr(x))  # Output: 'Sum(2, 2) # sum=3'
