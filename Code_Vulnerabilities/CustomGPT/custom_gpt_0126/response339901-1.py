
def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution finished.")

# Calling the function
divide(10, 2)  # No exception
divide(10, 0)  # Division by zero exception
