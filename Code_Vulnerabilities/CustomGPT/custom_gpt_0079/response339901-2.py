
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # Output: An error occurred: division by zero
else:
    print("This runs if no exceptions were raised")
finally:
    print("This runs no matter what")  # Always executed
