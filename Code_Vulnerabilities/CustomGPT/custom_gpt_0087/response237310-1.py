
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the base representation
        base_repr = f'Sum({self.a}, {self.b})'

        # Add comments only for human readability
        if self.sum != self.a + self.b:
            return f'{base_repr} # sum={self.sum}'  # This part will be ignored by Python parser
        else:
            return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Update the sum
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
