
try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
else:
    # This runs if the try block doesn't raise any exceptions
    print("No errors occurred.")
finally:
    # This will run no matter what
    print("Execution complete.")
