
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Generate a pretty-printed string with a hidden inconsistency detail
        inconsistent_message = '' if self.sum == self.a + self.b else f' # sum={self.sum}'
        return f'Sum({self.a}, {self.b}){inconsistent_message}'

    def __repr__(self):
        # The repr method returns a parseable expression
        return f'Sum({self.a}, {self.b})'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
print(repr(x)) # Output: 'Sum(2, 2)'
