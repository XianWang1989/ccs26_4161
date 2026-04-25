
try:
    result = 10 / 0  # This will raise ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # Prints: An error occurred: division by zero
else:
    print("No exceptions, result is:", result)
finally:
    print("This block always executes.")
