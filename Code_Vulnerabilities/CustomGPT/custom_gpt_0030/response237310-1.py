
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Check for consistency
        consistent = self.sum == self.a + self.b
        # Create a string that looks like a comment, but is valid Python syntax.
        return f'Sum({self.a}, {self.b})' + (f'  # sum={self.sum}' if not consistent else '')

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
x.update()  # Make sure to update the sum
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
