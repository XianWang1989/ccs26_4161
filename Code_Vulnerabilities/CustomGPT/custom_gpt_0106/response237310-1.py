
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the pretty-print output
        consistent_sum = self.a + self.b
        if self.sum == consistent_sum:
            return f'Sum({self.a}, {self.b})'
        else:
            # Add the inconsistency information in a way that can be ignored when parsing
            return f'Sum({self.a}, {self.b}) + " # sum={self.sum}"'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2) + " # sum=3"'
