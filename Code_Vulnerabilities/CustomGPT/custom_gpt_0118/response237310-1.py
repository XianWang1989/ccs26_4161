
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the printout
        base_str = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            # Including the inconsistency in the comment
            return f'{base_str} # sum={self.sum}'
        return base_str

    def pretty_print(self):
        # Return a valid Python expression that can be parsed
        return f'Sum({self.a}, {self.b})' + (f'  # sum={self.sum}' if self.sum != self.a + self.b else '')

# Demo
x = Sum(1, 2)
print(str(x))          # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))          # Output: 'Sum(2, 2) # sum=3'

# Gets the expression that can be parsed
print(x.pretty_print())  # Output: 'Sum(2, 2)  # sum=3'
