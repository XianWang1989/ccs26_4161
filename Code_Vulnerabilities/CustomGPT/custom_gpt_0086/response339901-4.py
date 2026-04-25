
try:
    # Division by zero will raise an exception
    result = 10 / 0
except Exception as e:
    # Capture the exception instance
    print(f"An error occurred: {e}")
else:
    # Execute if no exception occurred
    print(f"The result is {result}.")
finally:
    # Always executes
    print("Execution completed.")
