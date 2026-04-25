
class Sum:
    def __init__(self, a, b, _ignore=None):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        return 'Sum(%s, %s)%s' % (
            str(self.a), str(self.b),
            '' if self.sum == self.a + self.b else ' # sum=%s' % str(self.sum)
        )

# Usage
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2) # sum=3'

# Constructing a consistent object
consistent_repr = 'Sum(2, 2)'
# The _ignore parameter will not affect the constructor usage
inconsistent_after = str(Sum(2, 2, _ignore=x.sum))  # Outputs 'Sum(2, 2) # sum=3'
print(inconsistent_after)
