
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the pretty-print expression
        base_expression = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            # Embed the incorrect sum within a non-influential operation
            return f'{base_expression} + 0  # sum={self.sum}'
        return base_expression

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Ensure the sum is updated
print(str(x))  # Output: 'Sum(2, 2) + 0  # sum=3'
