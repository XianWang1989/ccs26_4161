
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")

# Usage
calc = Calculator()
result_add = calc.add(5, 3)
result_sub = calc.subtract(10, 4)
result_mul = calc.multiply(2, 7)
