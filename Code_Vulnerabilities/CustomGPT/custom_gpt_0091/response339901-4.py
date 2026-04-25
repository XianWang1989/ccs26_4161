
def risky_function():
    try:
        # Code that may raise an exception
        result = 10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        print(f"An error occurred: {e}")  # Accessing the exception
    else:
        print("No errors occurred. Result:", result)
    finally:
        print("This runs regardless of whether there was an error or not.")

risky_function()
