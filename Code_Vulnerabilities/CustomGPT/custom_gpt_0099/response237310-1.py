
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a string that can be parsed while also showing the inconsistency.
        invalid_sum = self.sum != self.a + self.b
        return f'Sum({self.a}, {self.b})' + (f'  # sum={self.sum}' if invalid_sum else '')

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
