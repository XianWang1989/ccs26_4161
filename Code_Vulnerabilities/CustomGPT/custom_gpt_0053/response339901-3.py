
import sys

try:
    # Code that could raise an exception
    a = 5 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")
    # Alternatively, using sys to capture the exception
    # e = sys.exc_info()[1]  
    # print(e)
else:
    print("No errors occurred, code executed successfully.")
finally:
    print("Executing the finally block, cleaning up resources.")
