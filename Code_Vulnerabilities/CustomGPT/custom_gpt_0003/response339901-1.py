
try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:  # Handle any Exception
    print(f"An error occurred: {e}")  # Accesses the error message from the caught exception
else:
    print("No exceptions occurred!")
finally:
    print("This block runs no matter what.")
