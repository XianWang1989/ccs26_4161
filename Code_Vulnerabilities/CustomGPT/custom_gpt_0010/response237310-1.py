
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a string representation that's parsable
        consistent_str = f'Sum({self.a}, {self.b})'
        inconsistency_info = '' if self.sum == self.a + self.b else f' /* sum={self.sum} */'
        return f'{consistent_str}{inconsistency_info}'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2) /* sum=3 */'
