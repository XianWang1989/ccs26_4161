
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Generate the construction expression
        construction = f'Sum({self.a}, {self.b})'

        # Check if sum is inconsistent
        if self.sum != self.a + self.b:
            return f'{construction}  # sum={self.sum}'  # This is a comment ignored by Python

        return construction

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
