
try:
    # Code that may cause an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
else:
    # This runs if the try block was successful
    print("The result is:", result)
finally:
    # This code always runs, regardless of exceptions
    print("Execution finished.")
