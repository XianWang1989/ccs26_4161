
try:
    # Some code that might cause an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # This prints "An error occurred: division by zero"
else:
    # This block runs only if no exceptions were raised
    print("The result is:", result)
finally:
    # This block runs regardless of what happened above
    print("This will always run.")
