
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Use '__repr__' to provide a version that is more formal and can be eval'd
        consistent_repr = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            return f"{consistent_repr}  # sum={self.sum} (inconsistent)"
        return consistent_repr

# Demo:
x = Sum(1, 2)
print(repr(x))  # Output: Sum(1, 2)

x.a = 2
print(repr(x))  # Output: Sum(2, 2)  # sum=3 (inconsistent)
