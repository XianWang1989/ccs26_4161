
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Example usage
divide_numbers(10, 2)  # Should print the result
divide_numbers(10, 0)  # Should print an error message
