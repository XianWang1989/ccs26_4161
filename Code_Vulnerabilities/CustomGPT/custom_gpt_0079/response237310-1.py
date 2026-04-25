
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the base string for the Sum object
        base_str = f'Sum({self.a}, {self.b})'

        # Check for inconsistency
        if self.sum != self.a + self.b:
            # Add a comment for human readability
            return f'{base_str} # sum={self.sum} (inconsistent)'

        return base_str

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()  # This updates the sum field
print(str(x))  # Output: Sum(2, 2) # sum=3 (inconsistent)
