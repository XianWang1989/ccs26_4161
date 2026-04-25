
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Format the constructor call
        constructor_call = f'Sum({self.a!r}, {self.b!r})'
        # Check if sum is inconsistent
        if self.sum != self.a + self.b:
            # Show inconsistency without breaking the parsing ability
            return f"{constructor_call}  # sum={self.sum!r} (inconsistent)"
        return constructor_call

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3 (inconsistent)'
