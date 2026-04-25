
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        # Represent the object consistently, but include 'inconsistency' info
        inconsistent_comment = f' # sum={self.sum}' if self.sum != self.a + self.b else ''
        return f'Sum({self.a}, {self.b}){inconsistent_comment.strip()}'

# Demo
x = Sum(1, 2)
print(repr(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(repr(x))  # Output: 'Sum(2, 2) # sum=3'
