
try:
    # Code that may raise an exception
    x = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}")  # This will output "An error occurred: division by zero"
else:
    print("No exceptions occurred!")
finally:
    print("This runs no matter what.")
