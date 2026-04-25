
try:
    # Code that may cause an exception
    result = 10 / 0
except Exception as e:
    # Handle the exception and print the error message
    print("An error occurred:", e)
else:
    # This runs if no exception occurs
    print("Result:", result)
finally:
    # This always runs, regardless of whether there was an exception
    print("Execution finished.")
