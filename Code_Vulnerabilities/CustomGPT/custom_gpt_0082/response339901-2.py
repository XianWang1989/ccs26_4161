
try:
    result = 10 / 0
except Exception:
    e = "An error occurred"  # You can't use 'Exception.something' directly
    print(e)
