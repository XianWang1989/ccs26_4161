
try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Catching the exception and printing it
else:
    print("No errors occurred.")  # Executes if no exceptions were raised
finally:
    print("This will always run.")  # Always executed regardless of an error
