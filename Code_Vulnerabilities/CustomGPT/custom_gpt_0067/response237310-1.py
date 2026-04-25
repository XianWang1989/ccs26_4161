
class Sum:
    def __init__(self, a, b, _debug_comment=None):
        self.a = a
        self.b = b
        self.update()
        if _debug_comment is not None:
            self._debug_comment = _debug_comment

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        debug_info = f" # sum={self.sum}" if self.sum != self.a + self.b else ""
        return f'Sum({self.a}, {self.b}, _debug_comment={debug_info})'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2, _debug_comment= # sum=3)'
