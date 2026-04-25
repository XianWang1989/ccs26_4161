
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Embed the human-readable inconsistency while ensuring valid Python syntax
        return 'Sum(%s, %s)  # sum=%s' % (
            str(self.a),
            str(self.b),
            '' if self.sum == self.a + self.b else str(self.sum)
        )

# Usage demonstration
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
