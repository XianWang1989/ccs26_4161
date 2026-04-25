
try:
    # Code that may raise an exception
    result = 10 / 2  # This will run successfully
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")  # This will execute only if no exceptions occur
finally:
    print("This will always execute regardless of success or failure.")
