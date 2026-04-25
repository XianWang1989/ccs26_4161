
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the consistent expression
        constructor_call = f'Sum({self.a}, {self.b})'

        # Check consistency
        if self.sum != self.a + self.b:
            # Display the wrong sum in a way that looks like a comment
            return f'{constructor_call}  # sum={self.sum} (inconsistent)'
        else:
            return constructor_call

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
x.update()  # Updating sum based on the new value of a
print(str(x))  # Output: 'Sum(2, 2)  # sum=3 (inconsistent)'
