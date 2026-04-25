
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Testing the function
divide_numbers(10, 2)  # Will print the result
divide_numbers(10, 0)  # Will print the error message
