
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct a string representation of the object
        consistent_call = f'Sum({self.a}, {self.b})'
        # Check if the sum is consistent
        if self.sum != self.a + self.b:
            # If inconsistent, use a special format
            return f'({consistent_call})  # sum={self.sum}'
        return consistent_call

# Demo
x = Sum(1, 2)
print(str(x))  # 'Sum(1, 2)'

x.a = 2
print(str(x))  # '(Sum(2, 2))  # sum=3'
