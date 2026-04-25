
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)
else:
    # This block executes if no exceptions are raised
    print("Result:", result)
finally:
    # This block always executes, regardless of an exception
    print("Execution completed.")
