
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # This will print the error message
else:
    print("No errors, result is:", result)
finally:
    print("This will always execute, regardless of errors.")
