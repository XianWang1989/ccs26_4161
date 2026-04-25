
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Prints the error message.
else:
    print("No exceptions occurred, this will run if try block is successful.")
finally:
    print("This will run no matter what.")  # Always executes.
