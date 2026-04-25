
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create the base string for the constructor
        base_str = f'Sum({self.a}, {self.b})'

        # Check if the sum is inconsistent
        if self.sum != self.a + self.b:
            # Append a note about the inconsistency
            return f"{base_str}  # sum={self.sum}"
        return base_str

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

# Introduce inconsistency
x.a = 2
x.update()  # Update the sum after changing 'a'
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
