
try:
    # Code that may raise an exception
    result = 10 / 5  # This will not raise an exception
except Exception as e:
    print(f"Error occurred: {e}")
else:
    print(f"Result is: {result}")  # This will execute since no exception occurred
finally:
    print("This will always execute.")
