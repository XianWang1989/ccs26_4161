
try:
    # code that may raise an exception
    num = int("not a number")  # This will raise a ValueError
except ValueError as e:
    print(f"Caught an error: {e}")
