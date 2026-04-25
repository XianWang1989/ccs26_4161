
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent = self.sum == self.a + self.b
        comment = f" # sum={self.sum}" if not consistent else ""
        return f'Sum({self.a}, {self.b}){comment}'

# Example usage:
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # Update sum to show inconsistency
print(str(x))  # Output: 'Sum(2, 2) # sum=3'
