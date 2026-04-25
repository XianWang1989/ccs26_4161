
try:
    # Attempt to divide by zero
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")  # Accessing the exception
else:
    print("Division successful: ", result)
finally:
    print("This will run no matter what.")
