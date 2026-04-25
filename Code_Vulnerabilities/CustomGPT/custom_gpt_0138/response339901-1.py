
try:
    # Some code that may raise an exception
    result = 10 / 0
except Exception as e:
    # Handle the exception and store it in 'e'
    print(f"An error occurred: {e}")
else:
    # Code that runs if no exceptions were raised
    print("The operation was successful:", result)
finally:
    # Code that runs no matter what (regardless of exceptions)
    print("This will always execute.")
