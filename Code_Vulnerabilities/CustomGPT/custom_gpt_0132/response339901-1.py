
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Prints the error message
else:
    print("No errors occurred, result is:", result)
finally:
    print("This block always runs.")
