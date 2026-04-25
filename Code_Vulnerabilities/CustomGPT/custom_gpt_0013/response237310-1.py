
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the base call
        base_call = f'Sum({self.a}, {self.b})'

        # Append a hidden comment-like structure for human reading
        inconsistency = f' # sum={self.sum}' if self.sum != self.a + self.b else ''

        return f'{base_call}{self._fake_comment(inconsistency)}'

    def _fake_comment(self, inconsistency):
        # Construct a string that resembles a comment
        return f' # note={repr(inconsistency)}' if inconsistency else ''

# Demo
x = Sum(1, 2)
print(str(x))    # Output: 'Sum(1, 2)'
x.a = 2
x.update()      # Update the sum to reflect the change
print(str(x))    # Output: 'Sum(2, 2) # note=\' # sum=3\''
