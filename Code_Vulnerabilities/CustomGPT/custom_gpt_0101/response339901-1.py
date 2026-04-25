
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    # This block executes if no exception occurs
    print("No errors encountered.")
finally:
    # This block always executes
    print("Execution completed.")
