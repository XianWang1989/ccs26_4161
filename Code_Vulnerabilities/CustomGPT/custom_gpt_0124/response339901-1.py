
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions, result:", result)
finally:
    print("This will always execute, whether an exception occurred or not.")
