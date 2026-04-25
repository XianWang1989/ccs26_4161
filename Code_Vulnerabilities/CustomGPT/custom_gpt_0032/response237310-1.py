
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Preparing a comment-like format in a way Python will ignore it
        consistency_comment = f", _inconsistent_sum={self.sum}" if self.sum != self.a + self.b else ""
        return f'Sum({self.a}, {self.b}{consistency_comment})'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()  # Update sum to be 4
print(str(x))  # Output: Sum(2, 2, _inconsistent_sum=4)
