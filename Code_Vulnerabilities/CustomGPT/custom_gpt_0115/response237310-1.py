
class Sum:
    def __init__(self, a, b, _inconsistent_comment=None):
        self.a = a
        self.b = b
        self.update()
        if _inconsistent_comment is not None:
            self.inconsistent_comment = f'  # {str(_inconsistent_comment)}'
        else:
            self.inconsistent_comment = ''

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        base_str = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            return f'{base_str}{self.inconsistent_comment} # sum={self.sum}'
        return base_str

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Outputs: 'Sum(2, 2)  #  # sum=3'
