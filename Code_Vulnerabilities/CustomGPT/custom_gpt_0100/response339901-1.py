
try:
    # Attempt to divide by zero, which will raise an exception
    result = 10 / 0
except Exception as e:
    # Print the exception message
    print(f"An error occurred: {e}")
else:
    # This block runs if no exceptions were raised
    print("Result is:", result)
finally:
    # This block runs no matter what
    print("Execution completed.")
