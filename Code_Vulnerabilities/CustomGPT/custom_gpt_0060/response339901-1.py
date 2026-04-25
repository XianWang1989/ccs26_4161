
try:
    # Simulating a division by zero error
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")  # Here, e will contain the exception message
else:
    print("No exceptions occurred, result is:", result)
finally:
    print("This block will always execute.")
