
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a consistent output while including inconsistency information
        data = f'Sum({self.a}, {self.b}, {self.sum})'
        return f"{data}  # Current sum: {self.sum} (actual: {self.a + self.b})"

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2, 3)  # Current sum: 3 (actual: 3)'

x.a = 2
x.update()  # Force a consistency check
print(str(x))  # Output: 'Sum(2, 2, 4)  # Current sum: 4 (actual: 4)'

# If inconsistent:
x.a = 2
x.b = 2  # Here, we make an inconsistency
x.sum = 3  # Incorrect sum
print(str(x))  # Output: 'Sum(2, 2, 3)  # Current sum: 3 (actual: 4)'
