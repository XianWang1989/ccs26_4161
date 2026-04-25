
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Use a temporary variable for the inconsistency
        inconsistency_info = ', sum={}'.format(self.sum) if self.sum != self.a + self.b else ''

        # Return the constructor call with the inconsistency at the end
        return 'Sum({}, {}){}'.format(self.a, self.b, inconsistency_info)

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)

x.a = 2
x.update()  # Manually trigger an update to 'sum'
print(str(x))  # Output: Sum(2, 2), sum=3
