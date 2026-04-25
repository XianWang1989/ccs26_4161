
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the formatted output
        normal_repr = f"Sum({self.a}, {self.b})"
        if self.sum != self.a + self.b:
            # Include the inconsistent value in a string format
            return f"{normal_repr}, ' # sum={self.sum}'"  # This part is a string for Python to ignore
        return normal_repr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Update to reflect new value
print(str(x))  # Output: "Sum(2, 2), ' # sum=3'"
