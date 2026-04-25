
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # This prints the error message
else:
    print("No exceptions occurred, result:", result)
finally:
    print("This block always executes, regardless of exceptions.")
