
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")  # e will contain the ZeroDivisionError message
    else:
        print(f"Result: {result}")  # Executed only if no exception occurs
    finally:
        print("Execution completed.")  # Always executes

# Test the function
divide(10, 2)  # Successful division
divide(10, 0)  # Division by zero
