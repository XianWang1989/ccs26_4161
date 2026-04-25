
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Composing the pretty-print output
        consistent_part = f'Sum({self.a}, {self.b})'
        # Use a dummy variable to encode the inconsistency
        inconsistent_note = f', _sum_is={self.sum}' if self.sum != self.a + self.b else ''
        return consistent_part + inconsistent_note

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2), _sum_is=3'
