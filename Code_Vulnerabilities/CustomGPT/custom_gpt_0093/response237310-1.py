
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent_repr = f'Sum({self.a}, {self.b})'
        # Include a comment displaying the sum if inconsistent
        if self.sum != self.a + self.b:
            return f'{consistent_repr}  # sum={self.sum}'
        return consistent_repr

# Demo
x = Sum(1, 2)
print(str(x))  # 'Sum(1, 2)'

x.a = 2
print(str(x))  # 'Sum(2, 2)  # sum=3'
