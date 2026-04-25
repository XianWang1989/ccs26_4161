
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # 'e' holds the error message
else:
    print("No errors occurred. Result:", result)
finally:
    print("This block always executes, regardless of errors.")
