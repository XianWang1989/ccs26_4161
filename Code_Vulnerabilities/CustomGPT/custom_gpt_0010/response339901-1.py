
def risky_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    else:
        print("Result is:", result)
    finally:
        print("Execution completed.")

# Example usage
risky_division(10, 2)  # Normal case
risky_division(10, 0)  # Will raise a ZeroDivisionError
