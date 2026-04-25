
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent_repr = 'Sum(%s, %s)' % (str(self.a), str(self.b))
        if self.sum != self.a + self.b:
            # Display the inconsistency without breaking Python parsing
            return consistent_repr + ' + " # sum=%s"' % str(self.sum)
        return consistent_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Outputs: 'Sum(2, 2) + " # sum=3"'
