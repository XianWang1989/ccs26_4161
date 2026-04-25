
try:
    # Some code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)  # Outputs: An error occurred: division by zero
else:
    print("No exceptions encountered!")
finally:
    print("This runs no matter what.")
