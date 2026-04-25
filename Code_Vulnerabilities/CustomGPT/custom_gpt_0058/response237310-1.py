
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a comment-like format for the inconsistency
        return 'Sum(%s, %s)  # sum=%s' % \
               (str(self.a), str(self.b),
                self.sum if self.sum == self.a + self.b else f"({self.sum})")

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)  # sum=3'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=(3)'
