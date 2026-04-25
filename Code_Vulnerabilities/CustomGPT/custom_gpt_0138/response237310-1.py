
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Use a comment that appears to be ignored in the expression
        return 'Sum(%s, %s)  # sum=%s' % (
            repr(self.a), repr(self.b), 
            self.sum if self.sum == self.a + self.b else self.sum
        )

# Demo
x = Sum(1, 2)
print(repr(x))  # Output: Sum(1, 2)  # sum=3
x.a = 2
print(repr(x))  # Output: Sum(2, 2)  # sum=3
