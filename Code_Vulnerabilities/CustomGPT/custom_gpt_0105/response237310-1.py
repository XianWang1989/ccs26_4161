
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent_part = f"Sum({self.a}, {self.b})"
        if self.sum != self.a + self.b:
            # We create a dummy variable within a tuple to allow a human-readable message.
            return f"{consistent_part} # sum={self.sum} (inconsistent)"
        return consistent_part

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
print(str(x))  # Output: Sum(2, 2) # sum=3 (inconsistent)
