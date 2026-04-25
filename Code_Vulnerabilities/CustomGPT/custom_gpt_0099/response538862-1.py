
def greet(name):
    """Greet the user by name."""
    print(f"Hello, {name}!")

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def main():
    greet("Alice")
    result = add(5, 3)
    print(f"Result of addition: {result}")

if __name__ == "__main__":
    main()
