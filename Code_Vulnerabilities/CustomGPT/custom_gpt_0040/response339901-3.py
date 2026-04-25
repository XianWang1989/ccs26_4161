
def risky_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")
    else:
        print(f"Result is: {result}")
    finally:
        print("Execution finished.")

# Example usage
risky_division(10, 0)  # Will trigger ZeroDivisionError
risky_division(10, 2)  # Will execute without exception
