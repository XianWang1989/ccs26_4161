
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Use a format that is parsable while embedding human-readable comments
        consistent_repr = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            # Embed inconsistency in a way Python will ignore
            return f"{consistent_repr}  # sum={self.sum} (inconsistent)"
        return consistent_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3 (inconsistent)'
