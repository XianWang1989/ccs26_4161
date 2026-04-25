
try:
    # Code that might raise an exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")  # Prints the error message
else:
    # Code to execute if no exception occurs
    print("Success:", result)
finally:
    # Code that runs no matter what
    print("Execution completed.")
