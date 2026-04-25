
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # e captures the exception
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This always runs, regardless of exceptions.")
