
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # Prints the error message
else:
    print("No error occurred, result is:", result)
finally:
    print("This block always executes, regardless of exceptions.")
