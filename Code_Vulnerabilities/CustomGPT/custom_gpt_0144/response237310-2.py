def ignore(*args):
    return None

class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __repr__(self):
        consistent_sum = self.a + self.b
        comment = ''
        if self.sum != consistent_sum:
            comment = f'  # sum={self.sum}, expected={consistent_sum}'
        return f'Sum({self.a}, {self.b}){comment}'

# Result is still valid Python, comments are ignored on parsing
