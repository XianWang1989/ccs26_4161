
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Generate the base constructor call
        base_call = 'Sum({}, {})'.format(repr(self.a), repr(self.b))

        # Check for inconsistency
        if self.sum != self.a + self.b:
            return f"{base_call}  # sum={repr(self.sum)}"
        return base_call

# Demo
x = Sum(1, 2)
print(str(x))  # 'Sum(1, 2)'

x.a = 2
print(str(x))  # 'Sum(2, 2)  # sum=3'
