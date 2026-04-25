
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        consistent_state = self.sum == self.a + self.b
        # Use a comment trick; Python will ignore what follows the semicolon
        return 'Sum(%s, %s); # sum=%s' % (
            str(self.a), 
            str(self.b), 
            str(self.sum) if not consistent_state else 'correct'
        )

# Demo:
x = Sum(1, 2)
print(str(x))  # Outputs: 'Sum(1, 2); # sum=3'
x.a = 2
print(str(x))  # Outputs: 'Sum(2, 2); # sum=3'
