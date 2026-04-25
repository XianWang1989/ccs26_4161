
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent = self.a + self.b
        return 'Sum(%s, %s)' % (str(self.a), str(self.b)) + \
               (self.add_comment(consistent))

    def add_comment(self, consistent):
        # Only include the comment if the sum is inconsistent
        if self.sum != consistent:
            return f' # sum={self.sum}'
        return ''

# Demo:
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Outputs: 'Sum(2, 2) # sum=3'
