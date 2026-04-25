
class Calculator:
    def add(self, a, b):
        """Returns the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Returns the quotient of a and b."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example of using the Calculator class
calc = Calculator()
result = calc.add(10, 5)
print("Addition Result:", result)
