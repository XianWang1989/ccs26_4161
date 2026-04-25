
try:
    value = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:  # Catches any Exception
    print(f"An error occurred: {e}")  # Prints the error message
else:
    print("No error occurred.")
finally:
    print("This block executes regardless of whether an exception occurred.")
