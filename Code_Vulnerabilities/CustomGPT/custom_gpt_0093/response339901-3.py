
try:
    # Potential code that might raise an exception
    result = 10 / 0  # Raises a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred; result is:", result)
finally:
    print("This block executes regardless of exceptions.")
