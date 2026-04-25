
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        correct_sum = self.a + self.b
        # Using a conditional expression to format the string
        return 'Sum({}, {}){}'.format(
            self.a,
            self.b,
            '' if self.sum == correct_sum else '  # sum={}'.format(self.sum)
        )

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
print(str(x))  # Output: 'Sum(2, 2)  # sum=3'
