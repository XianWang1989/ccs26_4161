
import sys

try:
    value = int(input("Enter a number: "))
    result = 100 / value
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    e = str(exc_value)  # Get the string representation of the exception
    print(f"An error occurred: {e}")
