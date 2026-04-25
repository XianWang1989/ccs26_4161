
class Sum:
    def __init__(self, a, b, *, _for_debugging=None):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Prepare the consistent expression
        expr = f'Sum({self.a}, {self.b})'
        # Append the inconsistency as a comment in a way that's safe for parsing
        if self.sum != self.a + self.b:
            return f'{expr}  # sum={self.sum}'
        return expr

# Demo:
x = Sum(1, 2)
print(str(x))  # 'Sum(1, 2)'
x.a = 2
print(str(x))  # 'Sum(2, 2)  # sum=3'

# Later, you can reconstruct the object as needed
# For example, parsing the string 'Sum(2, 2)' is still valid
