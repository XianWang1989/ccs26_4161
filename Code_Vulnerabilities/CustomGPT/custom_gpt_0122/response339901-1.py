
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handling the exception
    print(f"An error occurred: {e}")  # Accessing the exception message
else:
    # This block executes if no exception occurs
    print("Operation successful:", result)
finally:
    # This block always executes, regardless of exceptions
    print("Execution completed.")
