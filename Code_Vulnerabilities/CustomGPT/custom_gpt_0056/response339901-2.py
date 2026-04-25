
try:
    result = 10 / 0  # This will generate a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # e will contain the exception object
else:
    print("No errors occurred, result is:", result)
finally:
    print("This block always executes.")
