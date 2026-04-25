
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Use a representation that captures both the state and inconsistency
        return 'Sum(%s, %s) %s' % (
            str(self.a), str(self.b),
            ' # sum=%s' % str(self.sum) if self.sum != self.a + self.b else ''
        )

# Example usage:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
