
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a representation that includes a comment-like structure
        return 'Sum(%s, %s)%s' % (self.a, self.b,
               '' if self.sum == self.a + self.b else 
               ' /* inconsistent sum=%s */' % self.sum)

# Usage Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2) /* inconsistent sum=3 */'
