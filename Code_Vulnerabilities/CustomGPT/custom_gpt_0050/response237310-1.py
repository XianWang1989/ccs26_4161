
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        return 'Sum(%s, %s)%s' % (
            str(self.a), str(self.b),
            '' if self.sum == self.a + self.b else ' # sum=' + str(self.sum)
        )

    def __repr__(self):
        consistent_a = self.a
        consistent_b = self.b
        if self.sum != consistent_a + consistent_b:
            # Represent the consistent state, while adding an "inconsistent" comment
            return f"Sum({consistent_a}, {consistent_b})  # sum={self.sum}"
        return f"Sum({consistent_a}, {consistent_b})"

# Demo:
x = Sum(1, 2)
print(repr(x))  # Should print 'Sum(1, 2)'
x.a = 2
print(repr(x))  # Should print 'Sum(2, 2)  # sum=3'
