
try:
    # Simulate an error by dividing by zero
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)  # This will print the error message
else:
    print("Result:", result)  # This runs if no exception occurs
finally:
    print("This will always execute, regardless of an error")  # Always runs
