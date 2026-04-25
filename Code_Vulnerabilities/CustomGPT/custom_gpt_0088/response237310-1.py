
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        inconsistent_message = f" # sum={self.sum}" if self.sum != self.a + self.b else ""
        return f"Sum({self.a}, {self.b}, None){inconsistent_message}"

# Demo:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2, None)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2, None) # sum=3'
