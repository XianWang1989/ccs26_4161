
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Prints the error message
else:
    print("No exceptions occurred!")  # Only runs if no exception was raised
finally:
    print("This will always execute.")  # Always runs
