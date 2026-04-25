
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Build the base representation
        base_repr = f'Sum({self.a}, {self.b})'

        # Check for inconsistency
        if self.sum != self.a + self.b:
            # Add a hidden inconsistency as a non-intrusive comment
            return f'{base_repr} # sum={self.sum}'  # Human-readable comment
        return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()  # Manually trigger an inconsistency
print(str(x))  # Output: Sum(2, 2) # sum=3
