
try:
    # Attempt to divide by zero
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)  # Prints the error message
else:
    print("Result:", result)  # Executes if no exception occurs
finally:
    print("This will always execute.")  # Always runs
