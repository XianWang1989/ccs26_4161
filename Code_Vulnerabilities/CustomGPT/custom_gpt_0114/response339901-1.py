
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
else:
    # This block executes if no exceptions were raised
    print("No exceptions occurred, result is:", result)
finally:
    # This block always executes, regardless of exceptions
    print("Execution finished.")
