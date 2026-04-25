
class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b."""
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Example of using the Calculator
calc = Calculator()
print(calc.add(5, 3))
