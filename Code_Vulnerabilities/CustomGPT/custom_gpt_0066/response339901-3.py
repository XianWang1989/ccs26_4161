
def risky_operation():
    try:
        # Possible code that may raise an exception
        result = 10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        print("Caught an exception:", e)
    else:
        print("Operation successful, result is:", result)
    finally:
        print("This always executes, for cleanup.")

risky_operation()
