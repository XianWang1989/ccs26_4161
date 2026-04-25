
try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:  # Catches any exception
    print(f"An error occurred: {e}")  # Prints the error message
else:
    print("No errors occurred.")  # Executes if try block is successful
finally:
    print("This runs no matter what.")  # Always executes
