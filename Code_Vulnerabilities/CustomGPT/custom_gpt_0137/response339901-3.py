
import sys

def risky_code():
    # This function will raise an exception
    return 1 / 0  # Division by zero error

try:
    risky_code()
except Exception as e:
    print(f"An error occurred: {e}")  # handle the exception
else:
    print("No exceptions occurred. Code proceeded successfully.")
finally:
    print("This block runs regardless of exceptions.")
