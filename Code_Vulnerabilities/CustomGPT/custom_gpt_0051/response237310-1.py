
class Sum:
    def __init__(self, a, b, _comment=None):
        self.a = a
        self.b = b
        self.update()
        # Store the comment for debugging
        self.comment = _comment

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Format to show both the valid call and the comment
        consistent_call = 'Sum(%s, %s)' % (self.a, self.b)
        if self.sum != self.a + self.b:
            return '%s, _comment="%s"' % (consistent_call, self.sum)
        else:
            return consistent_call

# Demo usage:
x = Sum(1, 2)
print(str(x))  # 'Sum(1, 2)'

x.a = 2
print(str(x))  # 'Sum(2, 2), _comment="3"'
