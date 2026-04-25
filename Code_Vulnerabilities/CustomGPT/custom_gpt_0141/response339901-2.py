
def divide_numbers(x, y):
    try:
        result = x / y
    except Exception as e:
        print(f"An error occurred: {e}")  # Capturing and printing the exception
    else:
        print(f"The result is: {result}")  # Runs if no exception occurs
    finally:
        print("Execution complete.")  # Always runs

# Test with a zero division
divide_numbers(10, 0)
