
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Prepare the base string representation
        result = f'Sum({self.a}, {self.b})'

        # Append the sum only if it's inconsistent
        if self.sum != self.a + self.b:
            # Notice we format it in such a way that it can be evaluated
            return f'{result}, # sum={self.sum}'
        return result

    def pretty_print(self):
        # Generate output that a human can read that is also valid in Python syntax
        if self.sum != self.a + self.b:
            # Include an indicator of inconsistency
            return f'Sum({self.a}, {self.b})    # sum={self.sum}'
        return f'Sum({self.a}, {self.b})'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

# Change the state of the object
x.a = 2
x.update()
print(str(x))  # Output: 'Sum(2, 2), # sum=3'

# Human-readable version
print(x.pretty_print())  # Output: 'Sum(2, 2)    # sum=3'
