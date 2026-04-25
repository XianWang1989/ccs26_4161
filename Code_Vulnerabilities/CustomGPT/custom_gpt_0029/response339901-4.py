
def division(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Test the function
division(10, 2)  # Normal case
division(10, 0)  # This will raise an exception
