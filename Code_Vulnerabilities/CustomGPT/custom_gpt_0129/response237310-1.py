
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a human-readable string including the inconsistency
        is_inconsistent = self.sum != (self.a + self.b)
        inconsistency_info = f' # sum={self.sum}' if is_inconsistent else ''

        # Return a formatted string that looks like a constructor call
        return f'Sum({self.a}, {self.b}){inconsistency_info}'

# Example Usage
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
