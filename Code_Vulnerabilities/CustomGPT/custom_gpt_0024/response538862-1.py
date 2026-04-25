
class Calculator:
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example usage
calc = Calculator()
result = calc.add(5, 3)
print(result)
