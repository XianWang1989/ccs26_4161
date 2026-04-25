
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Catching the exception
else:
    print("No exceptions were raised!")
finally:
    print("This code always runs.")
