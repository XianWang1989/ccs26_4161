
import pickle

class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Create a consistent representation
        consistent_repr = f'Sum({self.a}, {self.b})'

        # If the object is inconsistent, add a comment
        if self.sum != self.a + self.b:
            return f'{consistent_repr} # sum={self.sum}'  # Human-readable part (comment)
        return consistent_repr  # Machine-readable part

    def __repr__(self):
        # Use pickle to show a consistent state
        return f'Sum{pickle.dumps((self.a, self.b))}'

# Demo
x = Sum(1, 2)
print(str(x))  # Output: Sum(1, 2)
x.a = 2
print(str(x))  # Output: Sum(2, 2) # sum=3
