
import sys

try:
    x = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")  # This will print the error message
else:
    print("No exceptions occurred!")  # Only runs if try block was successful
finally:
    print("This runs no matter what.")  # Always executed
