
try:
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {str(e)}")  # Access the exception message directly
