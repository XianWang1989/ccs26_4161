
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Build a formatted string representation
        consistent_expr = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            # Add a comment-like expression for pretty-printing
            return f'{consistent_expr}  # sum={self.sum} (inconsistent)'
        return consistent_expr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()  # Manually trigger update for demonstration
print(str(x))  # Output: Sum(2, 2)  # sum=3 (inconsistent)
