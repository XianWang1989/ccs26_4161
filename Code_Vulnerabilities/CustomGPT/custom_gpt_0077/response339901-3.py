
try:
    result = 10 / 0  # This will raise ZeroDivisionError.
except Exception as e:
    print(f"An error occurred: {e}")  # Handling the exception and printing it.
else:
    print("No errors, result is:", result)  # Executes only if no error occurred.
finally:
    print("This will always execute, regardless of errors.")  # Cleanup or final actions.
