
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        consistent_repr = f'Sum({self.a}, {self.b})'
        consistent = self.sum == self.a + self.b
        if consistent:
            return consistent_repr
        else:
            # Use a format that is still valid Python but will be ignored
            return f'{consistent_repr} # sum={self.sum} (inconsistent)'


# Demo: 
x = Sum(1, 2)
print(repr(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Assume we are in an inconsistent state now
print(repr(x))  # Output: 'Sum(2, 2) # sum=3 (inconsistent)'
