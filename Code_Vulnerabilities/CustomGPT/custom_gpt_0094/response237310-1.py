
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the expression in a valid format
        return 'Sum(%s, %s)' % (str(self.a), str(self.b)) + (
            '' if self.sum == self.a + self.b else '  # sum=%s' % str(self.sum))

    def pretty_print(self):
        # To print a valid expression with inconsistency showcased
        return 'Sum(%s, %s)' % (str(self.a), str(self.b)) + \
               ('  # Invalid sum: %s' % str(self.sum) if self.sum != self.a + self.b else '')

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'

# Inconsistent state pretty print
print(x.pretty_print())  # Output: 'Sum(2, 2)  # Invalid sum: 3'
