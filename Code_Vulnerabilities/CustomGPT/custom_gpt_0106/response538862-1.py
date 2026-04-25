
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else 'Error: Division by zero'

# Usage
calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
