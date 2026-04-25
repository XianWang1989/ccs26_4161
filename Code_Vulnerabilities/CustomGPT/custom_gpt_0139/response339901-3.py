
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Catch the exception and print the message
else:
    print("Division was successful!")  # Only runs if try block succeeds
finally:
    print("This block always runs, for cleanup actions.")  # Always runs

