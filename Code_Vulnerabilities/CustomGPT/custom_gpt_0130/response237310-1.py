
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a consistent representation
        consistent_repr = f'Sum({self.a}, {self.b})'
        # Check if the sum is inconsistent
        if self.sum != self.a + self.b:
            # Include the inconsistency notice using a format that Python ignores
            return f'{consistent_repr}  # sum={self.sum}'
        else:
            return consistent_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
