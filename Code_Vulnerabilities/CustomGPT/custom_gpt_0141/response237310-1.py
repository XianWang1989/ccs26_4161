
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Create a representation that is valid Python code
        consistent_repr = f'Sum({self.a}, {self.b})'

        # Check if the 'sum' is consistent with 'a' and 'b'
        if self.sum != self.a + self.b:
            return f'{consistent_repr}  # sum={self.sum} (inconsistent)'
        return consistent_repr

# Demo
x = Sum(1, 2)
print(repr(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Manually update after changing a
print(repr(x))  # Output: 'Sum(2, 2)  # sum=3 (inconsistent)'
