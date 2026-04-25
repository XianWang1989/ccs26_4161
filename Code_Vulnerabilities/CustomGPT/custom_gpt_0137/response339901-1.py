
try:
    # Code that may raise an exception
    risky_code()
except Exception as e:
    print(f"An error occurred: {e}")  # Accessing the exception message
else:
    print("No exceptions occurred. Code proceeded successfully.")
finally:
    print("This block runs regardless of exceptions.")
