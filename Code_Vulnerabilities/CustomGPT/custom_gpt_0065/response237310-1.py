
class Sum:
    def __init__(self, a, b, _comment=None):
        self.a = a
        self.b = b
        self.update()
        self._comment = _comment

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        comment = '' if self.sum == self.a + self.b else f' # sum={self.sum}'
        return f'Sum({self.a}, {self.b}, _comment={self._comment}){comment}'

# Example usage
x = Sum(1, 2)
print(str(x))   # Output: Sum(1, 2, _comment=None)
x.a = 2
print(str(x))   # Output: Sum(2, 2, _comment=None) # sum=3
