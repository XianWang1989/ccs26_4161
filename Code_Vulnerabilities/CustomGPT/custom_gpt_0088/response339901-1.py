
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

divide_numbers(10, 2)  # Normal case
divide_numbers(10, 0)  # Divison by zero case
