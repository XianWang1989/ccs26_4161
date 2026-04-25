
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception:
        e = "An error occurred: Division by zero or another exception."  # Manual assignment of the error
        print(e)
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")
