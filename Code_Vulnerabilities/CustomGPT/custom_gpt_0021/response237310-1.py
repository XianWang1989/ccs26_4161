
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        base_call = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            return f"{base_call}  # sum={self.sum}"
        return base_call

# Demo
x = Sum(1, 2)
print(repr(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(repr(x))  # Output: 'Sum(2, 2)  # sum=3'
