
try:
    # Trying to divide by zero
    result = 10 / 0
except Exception as e:
    # Printing the error message
    print(f"An error occurred: {e}")
else:
    # This will run if no exceptions occur
    print(f"The result is: {result}")
finally:
    # This block always executes, regardless of exceptions
    print("Execution complete.")
