
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Use a format that creates a parsable string 
        # while including a human-readable comment
        return f'Sum({self.a}, {self.b})' + \
               (f' # sum={self.sum}' if self.sum != self.a + self.b else '')

# Demo:
x = Sum(1, 2)
print(repr(x))  # Output: Sum(1, 2)
x.a = 2
print(repr(x))  # Output: Sum(2, 2) # sum=3
