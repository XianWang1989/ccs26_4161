
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

def main():
    calc = Calculator()
    result1 = calc.add(5, 3)  # Recently accessed method
    result2 = calc.subtract(10, 4)  # Another recently accessed method
    print(f"Addition: {result1}, Subtraction: {result2}")

if __name__ == "__main__":
    main()
