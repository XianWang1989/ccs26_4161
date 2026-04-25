
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    # Handle the exception and print the error message
    print("An error occurred:", e)
else:
    # Executes if no exception occurred
    print("Result:", result)
finally:
    # Always executes, regardless of whether an exception occurred
    print("Execution completed.")
