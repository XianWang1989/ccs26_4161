
try:
    # Code that may throw an exception
    value = int(input("Enter a number: "))  # This can raise ValueError
    result = 10 / value  # This can raise ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("This block always executes.")
