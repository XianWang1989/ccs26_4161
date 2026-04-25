
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.update()

    def update(self):
        self.sum = self.a + self.b

    def __str__(self):
        # Checks if the sum is consistent, appending a comment if it's not
        comment = f" # sum={self.sum}" if self.sum != self.a + self.b else ""
        return f"Sum({self.a}, {self.b}){comment}"

    def __repr__(self):
        # This should be valid Python code that can recreate the object
        return f"Sum({self.a}, {self.b})"  # Returns a parsable representation

# Demo
x = Sum(1, 2)
print(str(x))  # Output: 'Sum(1, 2)'

x.a = 2
x.update()  # To reflect the inconsistency in sum
print(str(x))  # Output: 'Sum(2, 2) # sum=4'

# Evaluating with `eval()` will recreate the consistent object:
eval_repr = repr(x)  # 'Sum(2, 2)'
x_reconstructed = eval(eval_repr)
print(x_reconstructed)  # Output: 'Sum(2, 2)'
