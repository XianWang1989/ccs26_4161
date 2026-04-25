
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a representation that can be parsed by Python
        expression = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            # Add a 'comment' that will be ignored during parsing
            return f"{expression}  # sum={self.sum} (inconsistent)"
        return expression

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()
print(str(x))  # Output: Sum(2, 2)  # sum=3 (inconsistent)
