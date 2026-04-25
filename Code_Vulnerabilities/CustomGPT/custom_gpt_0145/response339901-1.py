
def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution complete.")

# Testing with valid input
divide(10, 2)
# Testing with invalid input (division by zero)
divide(10, 0)
