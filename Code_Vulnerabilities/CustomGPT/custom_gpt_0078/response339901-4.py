
try:
    x = 1 / 0
except Exception:
    e = ZeroDivisionError("Custom message: Division by zero!")
    print(e)  # This will print: Custom message: Division by zero!
