
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the base string for a valid object representation
        base_repr = f'Sum({self.a}, {self.b})'
        # Check for inconsistency and format accordingly
        if self.sum != self.a + self.b:
            return f'{base_repr}  # sum={self.sum}'  # Uses a comment for human readability
        return base_repr

# Example usage
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
