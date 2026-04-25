
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Construct the base string for the call
        base_str = f'Sum({self.a}, {self.b})'
        # Check if the sum is consistent
        if self.sum != self.a + self.b:
            # Add a comment indicating the inconsistency
            return f"{base_str}  # sum={self.sum}"  # This comment will be ignored by Python
        return base_str

# Demo
x = Sum(1, 2)
print(str(x))  # Outputs: Sum(1, 2)
x.a = 2
print(str(x))  # Outputs: Sum(2, 2)  # sum=3
