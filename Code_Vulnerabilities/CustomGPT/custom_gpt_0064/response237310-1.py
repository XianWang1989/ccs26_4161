
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the base representation
        base_repr = 'Sum(%s, %s)' % (self.a, self.b)

        # Check for inconsistency and create a comment if needed
        if self.sum != self.a + self.b:
            return f'({base_repr}, _comment="sum={self.sum}")'

        return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2)'
x.a = 2
x.update()  # Ensure the sum is updated after modifying a
print(str(x))  # Outputs: 'Sum(2, 2), _comment="sum=3"'
