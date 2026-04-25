
try:
    # Code that might raise an exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred. Result:", result)
finally:
    print("This will execute regardless of an exception.")
