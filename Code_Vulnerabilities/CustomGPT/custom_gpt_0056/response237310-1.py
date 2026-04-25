
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Build the base constructor call
        base_str = 'Sum(%s, %s)' % (str(self.a), str(self.b))
        # Only add the comment if the sum is incorrect
        if self.sum != self.a + self.b:
            # Using `+` to concatenate strings and make it valid Python syntax
            return f"{base_str} + ' # sum={self.sum}'"
        return base_str

# Demo usage
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
print(str(x))  # Output: Sum(2, 2) + ' # sum=3'
