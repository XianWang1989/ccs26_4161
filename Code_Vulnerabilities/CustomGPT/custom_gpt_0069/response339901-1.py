
try:
    # Code that may cause an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # This will print the error message
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This block always executes.")
