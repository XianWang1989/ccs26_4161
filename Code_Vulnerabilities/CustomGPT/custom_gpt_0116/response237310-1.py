
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a base string containing constructor call
        constructor_call = f'Sum({self.a}, {self.b})'
        # Check consistency and construct the comment accordingly
        if self.sum != self.a + self.b:
            # Use an AST-style comment that is ignored by Python
            comment = f'  # sum={self.sum}'
            return f'{constructor_call}{comment}'
        return constructor_call

# Example usage
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
