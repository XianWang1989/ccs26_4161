
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        base_str = f'Sum({self.a}, {self.b})'
        if self.sum != self.a + self.b:
            return f"{base_str} # sum={self.sum}; inconsistent"
        return base_str

# Demonstration
x = Sum(1, 2)
print(str(x))  # Outputs: Sum(1, 2)

x.a = 2
x.update()  # Now manually trigger update to fix sum
print(str(x))  # Outputs: Sum(2, 2) # sum=3; inconsistent
