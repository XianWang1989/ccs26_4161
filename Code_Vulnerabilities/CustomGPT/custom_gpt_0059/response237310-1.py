
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a standard representation
        base_repr = f'Sum({self.a}, {self.b})'
        # Check for inconsistency
        if self.sum != self.a + self.b:
            # Print an 'inconsistency' in a way that Python will ignore
            return f'{base_repr} # ignore_sum={self.sum}'
        return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()
print(str(x))  # Output: 'Sum(2, 2) # ignore_sum=3'
