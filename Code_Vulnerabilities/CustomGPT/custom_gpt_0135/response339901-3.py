
try:
    result = 10 / 0  # Raises ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Will print the error
else:
    print("No errors occurred. Result:", result)
finally:
    print("This block always executes, cleaning up resources.")
