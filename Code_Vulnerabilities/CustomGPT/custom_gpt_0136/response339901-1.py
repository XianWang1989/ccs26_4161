
def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

divide(10, 0)  # This will raise a ZeroDivisionError
divide(10, 2)  # This will execute successfully
