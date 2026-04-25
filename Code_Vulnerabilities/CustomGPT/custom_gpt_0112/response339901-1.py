
try:
    value = int(input("Enter a number: "))  # This may raise a ValueError
    result = 10 / value                       # This may raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
