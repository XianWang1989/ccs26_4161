
def risky_operation():
    # This will raise an exception
    return 1 / 0  # Division by zero

try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Operation successful!")
finally:
    print("This will run no matter what.")
