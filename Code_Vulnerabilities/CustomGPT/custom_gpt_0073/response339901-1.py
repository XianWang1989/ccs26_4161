
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # e now contains the exception information
    print(f"An error occurred: {e}")
else:
    # Executes if no exception was raised
    print("Result:", result)
finally:
    # Executes no matter what, useful for cleanup actions
    print("Execution complete.")
