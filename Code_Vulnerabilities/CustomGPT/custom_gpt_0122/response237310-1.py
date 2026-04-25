
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent_expr = f'Sum({self.a}, {self.b})'
        inconsistency_comment = f' # sum={self.sum}' if self.sum != self.a + self.b else ''
        # Using `repr()` to construct a safer string that can be parsed
        return f'{consistent_expr}{inconsistency_comment}'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # This updates the sum to reflect inconsistency
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
