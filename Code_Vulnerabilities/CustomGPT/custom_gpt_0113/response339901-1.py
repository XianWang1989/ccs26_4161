
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
else:
    # This block executes if no exception occurs
    print(f"Result: {result}")
finally:
    # This block always executes, regardless of an exception
    print("Execution finished.")
