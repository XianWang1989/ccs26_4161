
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Prepare the parts of the representation
        base_repr = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            # Use a tuple to hold a comment as part of the expression
            comment_repr = f', # sum={self.sum}'  # This will just be a string
            final_repr = f'{base_repr}{comment_repr}'
            return f'({final_repr})'  # Make it a tuple so Python can handle it
        return base_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: '(Sum(2, 2), # sum=3)'
