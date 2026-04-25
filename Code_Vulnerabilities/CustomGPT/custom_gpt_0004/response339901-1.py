
try:
    # Code that might raise an exception
    result = 10 / 0
except Exception as e:
    # Catching the exception and assigning it to e
    print("An error occurred:", e)
else:
    # Code that runs if the try block succeeds without exceptions
    print("Result:", result)
finally:
    # Code that always runs, regardless of exceptions
    print("Execution completed.")
