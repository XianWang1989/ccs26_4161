
try:
    num = int(input("Enter a number: "))  # Might raise ValueError
    result = 10 / num                       # Might raise ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # This will print the error message
else:
    print(f"The result is {result}")   # Executes if no exception occurs
finally:
    print("Execution completed.")       # Always executes, regardless of exceptions
