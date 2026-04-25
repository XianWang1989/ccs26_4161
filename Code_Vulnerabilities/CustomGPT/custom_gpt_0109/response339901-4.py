
def risky_function():
    # This function might raise an exception
    return 1 / 0  # Intentional ZeroDivisionError

try:
    result = risky_function()
except Exception as e:
    print("An error occurred:", e)  # Handle the exception
else:
    print("No errors occurred. Result:", result)  # Only runs if no exception
finally:
    print("This code runs no matter what.")  # Cleanup code

# Output if an exception occurs will look like:
# An error occurred: division by zero
# This code runs no matter what.
