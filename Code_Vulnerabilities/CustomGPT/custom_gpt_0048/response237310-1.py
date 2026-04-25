
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Assemble the basic constructor format
        base_str = f'Sum({self.a}, {self.b})'

        # If there's an inconsistency, append a comment
        if self.sum != self.a + self.b:
            return f'{base_str} # sum={self.sum} (inconsistent)'

        return base_str

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Make the sum wrong intentionally
print(str(x))  # Output: 'Sum(2, 2) # sum=3 (inconsistent)'
