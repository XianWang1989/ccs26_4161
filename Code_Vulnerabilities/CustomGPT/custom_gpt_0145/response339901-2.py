
def divide(a, b):
    try:
        result = a / b
    except Exception:
        e = "An error occurred"
        print(e)
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution complete.")
