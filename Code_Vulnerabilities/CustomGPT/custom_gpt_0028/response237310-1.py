
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Create a consistent object representation
        consistent_repr = f'Sum({self.a}, {self.b})'

        # Check for inconsistency
        if self.sum != self.a + self.b:
            return f'{consistent_repr}  # sum={self.sum}'  # Comment visible to humans but ignored by Python

        return consistent_repr

# Demo
x = Sum(1, 2)
print(repr(x))  # Output: Sum(1, 2)

x.a = 2
print(repr(x))  # Output: Sum(2, 2)  # sum=3
