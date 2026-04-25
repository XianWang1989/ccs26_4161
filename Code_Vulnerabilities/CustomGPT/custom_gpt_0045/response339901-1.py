
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Testing the function with a potential division by zero
divide_numbers(10, 0)
