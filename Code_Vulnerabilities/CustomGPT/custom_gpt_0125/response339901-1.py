
try:
    x = 5 / 0  # This will raise an exception
except Exception as e:
    print(f"An error occurred: {e}")  # Print the error message
else:
    print("No errors occurred.")
finally:
    print("This runs regardless of errors.")
