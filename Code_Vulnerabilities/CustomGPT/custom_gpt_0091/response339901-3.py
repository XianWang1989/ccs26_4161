
try:
    # Simulate some error
    x = 1 / 0
except Exception as e:
    # e contains the exception instance
    print(e)  # This will print: division by zero
