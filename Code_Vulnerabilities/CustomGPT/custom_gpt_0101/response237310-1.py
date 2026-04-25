
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Use a format that Python can parse
        return 'Sum(%s, %s)%s' % (
            str(self.a), str(self.b),
            '' if self.sum == self.a + self.b else ' # sum=%s' % str(self.sum)
        ).replace('#', '  #')  # Ensure space after the comma for comment clarity

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
