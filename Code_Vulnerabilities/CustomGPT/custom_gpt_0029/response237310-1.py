
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a human-readable string that reveals inconsistencies
        consistent_part = f'Sum({self.a}, {self.b})'
        inconsistency_comment = '' if self.sum == self.a + self.b else f', # sum={self.sum}'
        # Format output to be valid Python syntax
        return f"{consistent_part}{inconsistency_comment if inconsistency_comment else ''}"

# Demo
x = Sum(1, 2)
print(str(x))    # Outputs: Sum(1, 2)
x.a = 2
print(str(x))    # Outputs: Sum(2, 2), # sum=3 (but this can't be parsed properly)

# Improved Output with invalid comment
class SumImproved:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Generate a valid expression for parsing
        consistent_part = f'Sum({self.a}, {self.b})'
        comment_part = f'  # inconsistency: sum={self.sum}' if self.sum != self.a + self.b else ''
        return f"{consistent_part}{comment_part}"

# Another Demo
y = SumImproved(2, 3)
y.a = 5
print(str(y))  # "Sum(5, 3)  # inconsistency: sum=8"
