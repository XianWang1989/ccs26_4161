
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
else:
    # This executes if no exception was raised
    print("No errors, result is:", result)
finally:
    # This code runs regardless of an exception
    print("Execution finished.")
