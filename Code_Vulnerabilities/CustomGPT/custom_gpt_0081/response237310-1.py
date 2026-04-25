
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Build a consistent expression string
        consistent_expr = f'Sum({self.a}, {self.b})'
        # Check if the computed sum is consistent and add inconsistency info as a string
        inconsistency_info = f' # sum={self.sum}' if self.sum != self.a + self.b else ''
        return f"{consistent_expr}{inconsistency_info}"

# Demonstration
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2)'

# Change value to create inconsistency
x.a = 2
print(str(x))  # Outputs: 'Sum(2, 2) # sum=3'
