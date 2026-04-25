
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Compose the basic constructor call
        output = f'Sum({self.a}, {self.b}'
        # Append a comment if the sum is inconsistent
        if self.sum != self.a + self.b:
            output += f', inconsistent_sum={self.sum}'
        output += ')'
        return output

# Example usage
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
print(str(x))  # Output: Sum(2, 2, inconsistent_sum=3)
