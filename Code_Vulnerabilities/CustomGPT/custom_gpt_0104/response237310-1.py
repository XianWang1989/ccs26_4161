
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a base representation
        base_repr = f'Sum({self.a}, {self.b})'

        # If the sum doesn't match the calculated value, indicate this for human readers
        if self.sum != self.a + self.b:
            return f'{base_repr}  # sum={self.sum} (Expected: {self.a + self.b})'
        return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

# Now let's simulate an inconsistency
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3 (Expected: 4)'
