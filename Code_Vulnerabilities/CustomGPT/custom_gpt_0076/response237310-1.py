
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Use a format that looks like a comment but is actually a valid expression
        comment = '' if self.sum == self.a + self.b else f'  # sum={self.sum}'
        return f'Sum({self.a}, {self.b}){comment}'

# Example demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
print(str(x))  # Output: Sum(2, 2)  # sum=3
