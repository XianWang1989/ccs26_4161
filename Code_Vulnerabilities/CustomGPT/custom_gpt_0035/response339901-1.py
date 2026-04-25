
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")  # This will print the error message.
else:
    print("No exceptions occurred.")
finally:
    print("This block runs no matter what.")
