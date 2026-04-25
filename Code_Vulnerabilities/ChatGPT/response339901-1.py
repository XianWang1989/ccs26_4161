
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")  # Catch specific exception and print message
    except Exception as e:  # Catch all other exceptions
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result is: {result}")  # Executes if no exceptions are raised
    finally:
        print("Execution of the try-except block is complete.")  # Always runs

# Test cases
divide(10, 2)  # This will print the result
divide(10, 0)  # This will catch ZeroDivisionError
divide(10, "a")  # This will catch a TypeError
