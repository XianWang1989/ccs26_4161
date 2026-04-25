
def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("The result is:", result)
    finally:
        print("Execution complete.")

divide(4, 2)  # Normal case
divide(4, 0)  # Will raise an exception
