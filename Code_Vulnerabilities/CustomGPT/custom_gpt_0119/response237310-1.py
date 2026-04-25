
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Using an extra parameter to wrap the inconsistency in parentheses
        return f'Sum({self.a}, {self.b}, _inconsistent_sum={self.sum})'

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2, _inconsistent_sum=3)

x.a = 2
print(str(x))  # Output: Sum(2, 2, _inconsistent_sum=3)
