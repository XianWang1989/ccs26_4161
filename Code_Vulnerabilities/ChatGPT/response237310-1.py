
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a pretty-printable representation
        return f'Sum({self.a}, {self.b})' + \
               (f' # sum={self.sum}' if self.sum != self.a + self.b else '')

    def to_expression(self):
        # Return a string that contains a valid Python expression representation
        consistent_sum = self.a + self.b
        return f'Sum({self.a}, {self.b})' + \
               ('' if self.sum == consistent_sum else f'  # sum={self.sum}')


# Example usage:
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()     # Manually update the sum field if needed
print(str(x))  # Output: Sum(2, 2) # sum=3

# Get a valid expression that can be executed
print(x.to_expression())  # Output: Sum(2, 2)  # sum=3
