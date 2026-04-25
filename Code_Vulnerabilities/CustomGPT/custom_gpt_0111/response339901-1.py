
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:  # Catch any Exception and store it in e
    print(f"An error occurred: {e}")
else:
    print("No errors occurred, result is:", result)
finally:
    print("This will always execute.")
