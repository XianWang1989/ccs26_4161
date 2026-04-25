
try:
    # Simulate some code that raises an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Handle the exception
else:
    print("Operation successful:", result)  # This runs if no exception was raised
finally:
    print("This will execute no matter what.")  # Cleanup code
