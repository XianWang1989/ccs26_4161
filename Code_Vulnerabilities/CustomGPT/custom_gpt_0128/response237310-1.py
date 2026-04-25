
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Generate the base representation of the object
        base_repr = 'Sum(%s, %s)' % (str(self.a), str(self.b))

        # Include inconsistency information if needed
        if self.sum != self.a + self.b:
            comment = '  # sum=%s' % str(self.sum)
            return f"{base_repr} + ' # INCONSISTENT: sum={self.sum}'"
        return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: Sum(1, 2) 
x.a = 2
print(str(x))  # Outputs: Sum(2, 2) + ' # INCONSISTENT: sum=3'
