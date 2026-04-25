
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        return 'Sum(%s, %s)' % (repr(self.a), repr(self.b))

    def __str__(self):
        # Format string that includes a human-readable inconsistency
        return f"{self.__repr__()} # sum={self.sum}" if self.sum != (self.a + self.b) else self.__repr__()

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
