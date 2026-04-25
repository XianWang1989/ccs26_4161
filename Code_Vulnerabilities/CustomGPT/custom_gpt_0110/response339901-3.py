
try:
    # Attempt to divide by a number
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("This code runs no matter what.")
