
try:
    # Simulating a division by zero error
    result = 10 / 0
except Exception:
    e = ZeroDivisionError("Division by zero is not allowed.")  # Manually creating an exception
    print(f"An error occurred: {e}")
finally:
    print("This block will always execute.")
