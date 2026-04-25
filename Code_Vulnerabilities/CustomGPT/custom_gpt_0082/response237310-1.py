
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Prepare the standard output
        output = f'Sum({self.a}, {self.b})'
        # Check for inconsistency
        if self.sum != self.a + self.b:
            output += f'  # sum={self.sum}'  # This part will be for human readers only
            return f'{output}, _comment_="This is inconsistent"'  # Python will parse this correctly
        return output

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: Sum(1, 2)
x.a = 2
print(str(x))  # Outputs: Sum(2, 2), _comment_="This is inconsistent" # sum=3
