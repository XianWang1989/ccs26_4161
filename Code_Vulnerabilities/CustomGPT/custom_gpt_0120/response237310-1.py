
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        details = f" # sum={self.sum}" if self.sum != self.a + self.b else ""
        return f"Sum({self.a}, {self.b}){details.lstrip()}"

    def __repr__(self):
        # This method ensures that we can reconstruct a consistent object
        return f"Sum({self.a}, {self.b})"

# Example usage
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)
x.a = 2
print(str(x))  # Output: Sum(2, 2) # sum=3
