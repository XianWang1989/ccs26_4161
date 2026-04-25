
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the base expression
        base_expression = f'Sum({self.a}, {self.b})'

        # Check for inconsistency and add comment if necessary
        if self.sum != self.a + self.b:
            # Using string to make it part of the expression
            return f'{base_expression} + " # sum={self.sum}"'
        else:
            return base_expression

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2) + " # sum=3"'
