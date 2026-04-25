
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Use a comment formatted as a string, concatenated, so it is ignored by Python
        return 'Sum(%s, %s)%s' % (
            str(self.a),
            str(self.b),
            '' if self.sum == self.a + self.b else ' + ("# sum=%s" % str(self.sum))'
        )

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
print(str(x))  # Output: Sum(2, 2) + ("# sum=3")
