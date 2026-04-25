
try:
    # Code that may cause an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handles the exception and assigns it to variable e
    print(f"An error occurred: {e}")
else:
    # Executes if no exception was raised in the try block
    print("The result is:", result)
finally:
    # This block always executes, regardless of an exception
    print("Execution complete.")
