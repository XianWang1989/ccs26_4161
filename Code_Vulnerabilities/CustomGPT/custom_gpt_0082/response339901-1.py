
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"Caught an exception: {e}")  # Will print the error message
else:
    print("No exceptions occurred, result:", result)
finally:
    print("This block executes no matter what.")
