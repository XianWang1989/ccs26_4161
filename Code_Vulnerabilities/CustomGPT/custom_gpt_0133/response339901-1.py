
def divide(x, y):
    try:
        result = x / y
    except Exception as e:  # Catch any exception and bind it to e
        print(f"An error occurred: {e}")  # Print the error message
        return None
    else:
        print("Division was successful!")
        return result
    finally:
        print("Execution completed.")  # This runs no matter what

# Example usage
value = divide(10, 0)  # This will raise a ZeroDivisionError
