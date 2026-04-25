
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Generate the expression for building the object
        base_expr = f'Sum({self.a}, {self.b})'
        # Check if the sum is consistent
        if self.sum != self.a + self.b:
            return f"{base_expr}  # sum={self.sum}"  # Including a comment
        return base_expr

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'
x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3' 
