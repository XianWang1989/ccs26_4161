
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred, result:", result)
finally:
    print("This will always execute, regardless of an error.")
