
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the base call string
        base_str = f'Sum({self.a}, {self.b})'

        # Determine if there's an inconsistency
        if self.sum != self.a + self.b:
            inconsistency_info = f" # sum={self.sum}"
            # Combine base string with inconsistency information
            return f"{base_str} + (# This indicates an inconsistency)"
        return base_str

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
print(str(x))  # Output: Sum(2, 2) + (# This indicates an inconsistency)
