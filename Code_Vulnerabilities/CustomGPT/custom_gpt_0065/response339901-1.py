
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Outputs the exception message
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This will always execute.")
