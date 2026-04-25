
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error occurred:", e)  # Print the error message
else:
    print("No exception occurred, result is:", result)
finally:
    print("This will always execute, regardless of exceptions.")
