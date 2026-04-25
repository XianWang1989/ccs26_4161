
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Formulate the representation that can rebuild the object.
        base_repr = f'Sum({self.a}, {self.b})'
        # Add a comment if the sum is inconsistent.
        if self.sum != self.a + self.b:
            comment = f'  # sum={self.sum}'
            return base_repr + comment
        return base_repr

# Demo usage
x = Sum(1, 2)
print(repr(x))  # Outputs: Sum(1, 2)
x.a = 2
print(repr(x))  # Outputs: Sum(2, 2)  # sum=3
