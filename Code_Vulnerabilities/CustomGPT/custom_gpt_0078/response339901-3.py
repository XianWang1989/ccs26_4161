
try:
    x = 1 / 0
except Exception:
    e = type(Exception("Custom message"))
    print(e)  # This will just show the type of the exception
