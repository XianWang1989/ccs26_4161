class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        consistent_sum = self.a + self.b
        if self.sum == consistent_sum:
            return f'Sum({self.a}, {self.b})'
        else:
            return f'Sum({self.a}, {self.b})  # Inconsistent: sum={self.sum}, expected={consistent_sum}'

    def __str__(self):
        return self.__repr__()

# Usage demo
x = Sum(1, 2)
print(repr(x))  # Sum(1, 2)

x.a = 2
print(repr(x))  # Sum(2, 2)  # Inconsistent: sum=3, expected=4
