
try:
    # Some risky code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions, result is:", result)
finally:
    print("This will always execute, regardless of exceptions.")
